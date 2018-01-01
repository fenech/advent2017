import functools

class KnotHasher:
    LENGTH = 256

    def __init__(self, input):
        self.lengths = list(map(ord, input)) + [17, 31, 73, 47, 23]

        self.string = list(range(self.LENGTH))
        self.position = 0
        self.skip = 0

    def twist(self, length):
        replacements = list(self.string[(self.position + i) % self.LENGTH] for i in range(length))

        for i in range(length):
            self.string[(self.position + length - i - 1) % self.LENGTH] = replacements[i]

        self.position = self.position + length + self.skip
        self.skip += 1

    def dense_hash(self):
        for i in range(64):
            for length in self.lengths:
                self.twist(length)

        sparse_hash = self.string
        return (functools.reduce(lambda a, b: a ^ b, sparse_hash[i*16:i*16+16]) for i in range(16))


    def knot_hash(self):
        return "".join(map(lambda x: format(x, '02x'), self.dense_hash()))

if __name__ == "__main__":
    s = "102,255,99,252,200,24,219,57,103,2,226,254,1,0,69,216"
    hasher = KnotHasher(s)
    print(hasher.knot_hash())
