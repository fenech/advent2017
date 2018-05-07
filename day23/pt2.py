def is_prime(num):
    for i in range(2, int(num ** 0.5)):
        if num % i == 0:
            return False
    return True

h = sum(not is_prime(i) for i in range(105700, 122701, 17))
print(h)
