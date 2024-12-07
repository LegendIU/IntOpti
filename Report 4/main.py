def bisection_method(func, a, b, epsilon):
    if func(a) * func(b) > 0:
        raise ValueError("The function must have different signs at the ends of the interval [a, b].")

    while (b - a) / 2 > epsilon:
        c = (a + b) / 2
        if abs(func(c)) < epsilon:
            return c
        elif func(a) * func(c) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2


def f(x):
    return x**3 - 6*x**2 + 11*x - 6


a = 1.0
b = 2.0
epsilon = 1e-6

try:
    root = bisection_method(f, a, b, epsilon)
    print(f"Approximate root: {root}")
except ValueError as e:
    print(e)
