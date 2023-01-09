# best practices fibonacci


def fibonacci(n):
    a = 0
    b = 1
    if n <= 0:
        return a
    elif n == 1:
        return b

    for i in range(1, n):
        a, b = b, a + b
    return b
