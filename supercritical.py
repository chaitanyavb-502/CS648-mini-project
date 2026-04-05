import networkx as nx
import matplotlib.pyplot as plt

# ================= PARAMETERS =================
n = 1000
epsilon = 0.5
p = (1 + epsilon) / n

iterations = 200

giant_sizes = []

# ================= SIMULATION =================

for _ in range(iterations):
    G = nx.erdos_renyi_graph(n, p)

    largest = max(len(c) for c in nx.connected_components(G))
    giant_sizes.append(largest)

# ================= REFERENCE LINE =================

ref_line = (epsilon * n) / 2

# ================= PLOT =================

plt.figure(figsize=(10, 6))

plt.scatter(range(iterations), giant_sizes, s=12, alpha=0.7,
            label="Largest Component Size")

# horizontal line at εn/2
plt.axhline(ref_line, color='red', linestyle='--',
            label=f"εn/2 ≈ {int(ref_line)}")

plt.xlabel("Iteration")
plt.ylabel("Largest Component Size")

plt.title(f"Supercritical Phase: p = (1 + ε)/n, ε = {epsilon}, n = {n}")

plt.legend()
plt.grid()

plt.show()
