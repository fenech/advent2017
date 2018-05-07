tape = set()
slot = 0
state = 'A'

for i in range(12629077):
    if state is 'A':
        if slot not in tape:
            tape |= {slot}
            slot += 1
            state = 'B'
        else:
            tape -= {slot}
            slot -= 1
            state = 'B'
    elif state is 'B':
        if slot not in tape:
            slot += 1
            state = 'C'
        else:
            slot -= 1
            state = 'B'
    elif state is 'C':
        if slot not in tape:
            tape |= {slot}
            slot += 1
            state = 'D'
        else:
            tape -= {slot}
            slot -= 1
            state = 'A'
    elif state is 'D':
        if slot not in tape:
            tape |= {slot}
            slot -= 1
            state = 'E'
        else:
            slot -= 1
            state = 'F'
    elif state is 'E':
        if slot not in tape:
            tape |= {slot}
            slot -= 1
            state = 'A'
        else:
            tape -= {slot}
            slot -= 1
            state = 'D'
    elif state is 'F':
        if slot not in tape:
            tape |= {slot}
            slot += 1
            state = 'A'
        else:
            slot -= 1
            state = 'E'

print(len(tape))
