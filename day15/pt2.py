def sequence(value, factor, power):
    while True:
        value *= factor
        value %= 2147483647
        if not value & (2 ** power - 1):
            yield value

a = sequence(883, 16807, 2)
b = sequence(879, 48271, 3)

score = 0

for i, (a, b) in enumerate(zip(a, b)):
    if i == 5e6:
        break
    score += not((a^b) & 0xffff)

print(score)
