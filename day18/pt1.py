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
"""

import re

class Processor:
    def __init__(self, instructions):
        self.registers = {}
        self.instructions = instructions
        self.current_line = 0
        self.actions = [
            (r'snd (\w)', self.sound),
            (r'rcv (\w)', self.recover),
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

    def sound(self, match):
        target, = match.groups()
        self.frequency = self.value(target)

    def set_register(self, match):
        target, value = match.groups()
        self.registers[target] = self.value(value)

    def add_register(self, match):
        target, value = match.groups()
        self.registers[target] = self.registers.get(target, 0) + self.value(value)

    def mul_register(self, match):
        target, value = match.groups()
        self.registers[target] = self.registers.get(target, 0) * self.value(value)

    def mod_register(self, match):
        target, value = match.groups()
        self.registers[target] = self.registers.get(target, 0) % self.value(value)

    def recover(self, match):
        target, = match.groups()
        if self.registers[target]:
            return self.frequency

    def jump(self, match):
        target, value = match.groups()
        if self.value(target) > 0:
            self.current_line += self.value(value) - 1

    def process(self, instruction):
        for pattern, action in self.actions:
            m = re.match(pattern, instruction)
            if m is not None:
                return action(m)

    def process_all(self):
        while 0 <= self.current_line < len(self.instructions):
            result = self.process(self.instructions[self.current_line])
            if result is not None:
                return result
            self.current_line += 1

processor = Processor(s.splitlines())

print(processor.process_all())
