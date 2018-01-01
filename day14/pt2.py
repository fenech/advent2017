from pt1 import BinaryKnotHasher

LENGTH = 128

def process_queue(queue, grid, labelled):
    while queue:
        cx, cy = queue.pop(0)
        neighbours = [
            (cx - 1, cy),
            (cx + 1, cy),
            (cx, cy - 1),
            (cx, cy + 1)
        ]

        for i, j in ((i, j) for i, j in neighbours if i >= 0 and i < LENGTH and j >= 0 and j < LENGTH):
            try:
                pixel = grid[j][i]
            except IndexError:
                continue

            if pixel and (i, j) not in labelled:
                labelled.add((i, j))
                queue.append((i, j))



def find_regions(grid):
    queue = []
    label = 0
    labelled = set()

    for j, row in enumerate(grid):
        for i, pixel in enumerate(row):
            if pixel and (i, j) not in labelled:
                label += 1
                labelled.add((i, j))
                queue.insert(0, (i, j))
                process_queue(queue, grid, labelled)

    return label

if __name__ == "__main__":
    s = "hxtvlmkl"

    grid = []
    for row in range(LENGTH):
        hasher = BinaryKnotHasher("{}-{}".format(s, row))
        grid.append(list(map(int, hasher.bin_knot_hash())))

    print(find_regions(grid))
