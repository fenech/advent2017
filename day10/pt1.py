s = "102,255,99,252,200,24,219,57,103,2,226,254,1,0,69,216"

state = {
    'string': list(range(256)),
    'position': 0,
    'skip': 0
}

def twist(state, length):
    string = state['string']
    position = state['position']
    skip = state['skip']

    replacements = list(string[(position + i) % len(string)] for i in range(length))

    for i in range(length):
        string[(position + length - i - 1) % len(string)] = replacements[i]

    return {
        'string': string,
        'position': position + length + skip,
        'skip': skip + 1
    }

for length in map(int, s.split(",")):
    state = twist(state, length)

a, b = state['string'][:2]
print(a * b)
