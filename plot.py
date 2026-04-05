import matplotlib.pyplot as plt
import numpy as np

N = 1000  # same as C++

edges = []
largest = []

with open("data.txt") as f:
    for line in f:
        e, mx = map(float, line.split())
        edges.append(e)
        largest.append(mx)

# ===== Experimental curve =====
c_exp = [2 * e / N for e in edges]     # c = 2m/n
y_exp = [mx / N for mx in largest]     # L1/n

# ===== Theoretical curve =====
def rho(c):
    if c <= 1:
        return 0.0
    x = 0.5
    for _ in range(100):
        x = 1 - np.exp(-c * x)
    return x

c_vals = np.linspace(0, max(c_exp), 300)
rho_vals = [rho(c) for c in c_vals]

# ===== Plot =====
plt.figure(figsize=(8,5))

plt.plot(c_exp, y_exp, label="Simulation", alpha=0.7)
plt.plot(c_vals, rho_vals, linestyle='--', label="Theory")

plt.axvline(x=1, linestyle=':', label='c = 1 (phase transition)')

plt.xlabel("c = 2m / n")
plt.ylabel("Largest Component Fraction (L1 / n)")
plt.title("Giant Component: Theory vs Simulation")

plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
