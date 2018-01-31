step = 344
position = 0

current = None

for i in range(50000000):
    position = (position + step) % (i + 1)
    if position == 0:
        current = i + 1
    position = (position + 1) % (i + 2)

print(current)
