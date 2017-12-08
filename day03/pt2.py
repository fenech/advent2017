max_spiral = 430

memory = [[0 for x in range(max_spiral * 2 + 1)] for y in range(max_spiral * 2 + 1)]

(start_x, start_y) = (max_spiral, max_spiral)

memory[start_x][start_y] = 1

def spiral_gen(x, y):
    for size in range(1, max_spiral):
        for step in range(size):
            yield (x + size, y + step)
        for step in range(size, -size, -1):
            yield (x + step, y + size)
        for step in range(size, -size, -1):
            yield (x - size, y + step)
        for step in range(-size, size + 1):
            yield (x + step, y - size)
        for step in range(-size, 0):
            yield (x + size + 1, y + step)

for x, y in spiral_gen(start_x, start_y):
    value = sum(memory[i][j] for i in range(x - 1, x + 2) for j in range(y - 1, y + 2))
    if value >= 312051:
        print(value)
        break
    memory[x][y] = value
