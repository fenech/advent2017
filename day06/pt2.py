s = """5	1	10	0	1	7	13	14	3	12	8	10	7	12	0	6"""

numbers = list(map(int, s.split()))
length = len(numbers)

seen = set([tuple(numbers)])

step = 0
loop = 0

while True:
    step += 1
    highest = max(numbers)
    index = numbers.index(highest)
    numbers[index] = 0

    for i in range(index + 1, index + highest + 1):
        numbers[i % length] += 1

    t = tuple(numbers)

    if t in seen:
        loop += 1

        if loop == 2:
            print(step)
            break

        seen = set()
        step = 0

    seen.add(t)
