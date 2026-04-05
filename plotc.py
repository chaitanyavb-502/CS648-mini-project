import matplotlib.pyplot as plt
import math

N = 1000

runs = {}
connected_points = {}

# ================= READ DATA =================
with open("data.txt") as f:
    for line in f:
        if line.startswith("#"):
            _, _, run, val = line.split()
            connected_points[int(run)] = int(val)
            continue

        run, e, comp = map(int, line.split())

        if run not in runs:
            runs[run] = ([], [])

        runs[run][0].append(e)
        runs[run][1].append(comp)

# ================= PLOT =================

plt.figure(figsize=(10, 6))

# plot each run
for run in runs:
    x, y = runs[run]
    plt.plot(x, y, alpha=0.5)

# theoretical vertical lines
plt.axvline(N/2, color='red', linestyle='--', label='m = n/2')
plt.axvline(2*N, color='green', linestyle='--', label='m = 2n')
plt.axvline((N/2)*math.log(N), color='black', linestyle='--', label='(n/2) log n')

# connectivity points
for run in connected_points:
    plt.axvline(connected_points[run], color='purple', alpha=0.2)

plt.xlabel("Number of Edges (m)")
plt.ylabel("Number of Connected Components")

plt.title("Components vs Edges (Multiple Runs)")

plt.legend()
plt.grid()

plt.show()
