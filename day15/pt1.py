def sequence(value, factor):
    while True:
        value *= factor
        value %= 2147483647
        yield value

a = sequence(883, 16807)
b = sequence(879, 48271)

score = 0

for i, (a, b) in enumerate(zip(a, b)):
    if i == 4e7:
        break
    score += not((a^b) & 0xffff)

print(score)
