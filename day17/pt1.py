step = 344
buffer = [0]
position = 0

for i in range(2017):
    position = (position + step) % len(buffer)
    buffer[position + 1:position + 1] = [i + 1]
    position = (position + 1) % len(buffer)

print(buffer[position + 1])
