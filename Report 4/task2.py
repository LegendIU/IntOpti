def f(x):
    return (x - 2)**2 + 3

def golden_section_search(a, b, epsilon):
    gr = (5**0.5 - 1) / 2
    c = b - (b - a) * gr
    d = a + (b - a) * gr
    while (b - a) > epsilon:
        if f(c) < f(d):
            b = d
            d = c
            c = b - (b - a) * gr
        else:
            a = c
            c = d
            d = a + (b - a) * gr
    x_min = (a + b) / 2
    return x_min, f(x_min)

x_min, f_min = golden_section_search(0, 5, 1e-4)
print("Approximate x_min:", x_min)
print("Minimum value f(x_min):", f_min)

print("\nAdditional Question 1:")
print("Why does the Golden Section Method work only for unimodal functions?")
print("Answer: The method assumes the function has a single minimum (unimodal) within the interval.")
print("It relies on narrowing down the interval while maintaining the unimodal property.")
print("For multimodal functions, the method may converge to a local minimum or fail to find the global minimum.")
