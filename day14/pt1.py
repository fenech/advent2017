import sys, os

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(dir_path, '..'))

from day10.pt2 import KnotHasher

class BinaryKnotHasher(KnotHasher):
    def bin_knot_hash(self):
        return "".join(map(lambda x: format(int(x, 16), '04b'), self.knot_hash()))

if __name__ == "__main__":
    s = "hxtvlmkl"

    used = 0
    for row in range(128):
        hasher = BinaryKnotHasher("{}-{}".format(s, row))
        used += sum(int(x) for x in hasher.bin_knot_hash())

    print(used)
