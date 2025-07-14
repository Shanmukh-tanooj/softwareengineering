import numpy as np

x_values = []
y_values = []

for i in range(3):
    x = float(input(f"Enter hour x{i+1}: "))
    y = float(input(f"Enter temperature at hour {x}: "))
    x_values.append(x)
    y_values.append(y)

A = np.array([[x**2, x, 1] for x in x_values])
B = np.array(y_values)

a, b, c = np.linalg.solve(A, B)

print(f"\nQuadratic model: y = {a:.4f}x^2 + {b:.4f}x + {c:.4f}\n")

def temperature_at(x):
    return a * x**2 + b * x + c

print("Temperatures at input hours:")
for x in x_values:
    print(f"{int(x):02d}:00 -> {temperature_at(x):.2f}°C")
