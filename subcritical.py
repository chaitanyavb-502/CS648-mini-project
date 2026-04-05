import networkx as nx
import matplotlib.pyplot as plt
import math

n = 1000
epsilon = 0.5
p = (1 - epsilon) / n

iterations = 200

giant_sizes = []

for _ in range(iterations):
    G = nx.erdos_renyi_graph(n, p)

    largest = max(len(c) for c in nx.connected_components(G))
    giant_sizes.append(largest)

log_bound = (7 * math.log(n)) / (epsilon ** 2)

plt.figure(figsize=(10, 6))

plt.scatter(range(iterations), giant_sizes, s=12, alpha=0.7,
            label="Largest Component Size")

plt.axhline(log_bound, color='red', linestyle='--',
            label=f"7 ln(n) / ε² ≈ {int(log_bound)}")

plt.axhline(math.log(n), color='green', linestyle='--',
            label="ln(n)")

plt.xlabel("Iteration")
plt.ylabel("Largest Component Size")

plt.title(f"Subcritical Phase: p = (1 - ε)/n, ε = {epsilon}, n = {n}")

plt.legend()
plt.grid()

plt.show()
