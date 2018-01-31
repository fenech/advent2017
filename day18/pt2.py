s = """set i 31
set a 1
mul p 17
jgz p p
mul a 2
add i -1
jgz i -2
add a -1
set i 127
set p 316
mul p 8505
mod p a
mul p 129749
add p 12345
mod p a
set b p
mod b 10000
snd b
add i -1
jgz i -9
jgz a 3
rcv b
jgz b -1
set f 0
set i 126
rcv a
rcv b
set p a
mul p -1
add p b
jgz p 4
snd a
set a b
jgz 1 3
snd b
set f 1
add i -1
jgz i -11
snd a
jgz f -16
jgz a -19
""".splitlines()

import re

class Processor:
    def __init__(self, instructions, messageBus, pid):
        self.instructions = instructions
        self.messageBus = messageBus
        self.pid = pid
        self.registers = { 'p': pid }
        self.current_line = 0
        self.actions = [
            (r'snd (\w)', self.send),
            (r'rcv (\w)', self.receive),
            (r'set (\w) ([-\w]+)', self.set_register),
            (r'add (\w) ([-\w]+)', self.add_register),
            (r'mul (\w) ([-\w]+)', self.mul_register),
            (r'mod (\w) ([-\w]+)', self.mod_register),
            (r'jgz (\w) ([-\w]+)', self.jump)
        ]

    def value(self, value):
        try:
            return int(value)
        except ValueError:
            return self.registers.get(value, 0)

    def send(self, match):
        target, = match.groups()
        self.messageBus.send(self.value(target), self.pid)
        self.current_line += 1

    def set_register(self, match):
        target, value = match.groups()
        self.registers[target] = self.value(value)
        self.current_line += 1

    def add_register(self, match):
        target, value = match.groups()
        self.registers[target] = self.registers.get(target, 0) + self.value(value)
        self.current_line += 1

    def mul_register(self, match):
        target, value = match.groups()
        self.registers[target] = self.registers.get(target, 0) * self.value(value)
        self.current_line += 1

    def mod_register(self, match):
        target, value = match.groups()
        self.registers[target] = self.registers.get(target, 0) % self.value(value)
        self.current_line += 1

    def receive(self, match):
        target, = match.groups()
        message = self.messageBus.check(self.pid)
        if message is not None:
            self.registers[target] = message
            self.current_line += 1

    def jump(self, match):
        target, value = match.groups()
        if self.value(target) > 0:
            self.current_line += self.value(value)
        else:
            self.current_line += 1

    def process(self):
        instruction = self.instructions[self.current_line]
        for pattern, action in self.actions:
            m = re.match(pattern, instruction)
            if m is not None:
                return action(m)

class MessageBus:
    def __init__(self):
        self.messages = []
        self.sendCounts = {}
        self.waiting = set()

    def send(self, message, origin):
        self.messages.append({
            'msg': message,
            'origin': origin
        })
        self.sendCounts[origin] = self.sendCounts.get(origin, 0) + 1

    def check(self, origin):
        try:
            self.waiting.add(origin)
            message = next(msg for msg in self.messages if msg['origin'] != origin)
            self.messages.remove(message)
            self.waiting.remove(origin)
            return message['msg']
        except StopIteration:
            return None

messageBus = MessageBus()
processors = [Processor(s, messageBus, i) for i in range(2)]

while len(messageBus.waiting) < 2:
    for p in processors:
        p.process()

print(messageBus.sendCounts[1])
