import numpy as np

x_values = [6, 12, 18]
y_values = [20, 32, 22]

A = np.array([[x**2, x, 1] for x in x_values])
B = np.array(y_values)

a, b, c = np.linalg.solve(A, B)

def temperature_at(x):
    return a * x**2 + b * x + c

for x in x_values:
    y = temperature_at(x)
    print(f"x = {x}, y = {y:.2f}")
