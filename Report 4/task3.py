def f(x):
    return -x**2 + 4*x + 1

def gradient_ascent(x0, alpha, N):
    x = x0
    for _ in range(N):
        grad = -2*x + 4
        x = x + alpha * grad
    return x, f(x)

x_max, f_max = gradient_ascent(0, 0.1, 100)
print("Approximate x_max:", x_max)
print("Maximum value f(x_max):", f_max)

print("\nAdditional Question 1:")
print("How does the choice of α affect convergence?")
print("Answer: The learning rate α affects both the speed and stability of convergence.")
print("A small α may lead to slow convergence, while a large α can cause overshooting and divergence.")
print("Choosing an appropriate α is crucial for the method to converge efficiently to the maximum.")
    