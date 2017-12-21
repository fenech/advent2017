import functools

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

lengths = list(map(ord, s)) + [17, 31, 73, 47, 23]

for i in range(64):
    for length in lengths:
        state = twist(state, length)

sparse_hash = state['string']

dense_hash = (functools.reduce(lambda a, b: a ^ b, sparse_hash[i*16:i*16+16]) for i in range(16))

print("".join(map(lambda x: format(x, '02x'), dense_hash)))
