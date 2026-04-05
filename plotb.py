import matplotlib.pyplot as plt

N = 1000

# store data
runs = {}
connected_points = {}

with open("data.txt") as f:
    for line in f:
        if line.startswith("#"):
            _, _, run, val = line.split()
            connected_points[int(run)] = int(val)
            continue

        run, e, sz = map(int, line.split())
        if run not in runs:
            runs[run] = ([], [])
        runs[run][0].append(e)
        runs[run][1].append(sz)

# ================= PLOT =================

plt.figure(figsize=(10, 6))

# plot each run
for run in runs:
    x, y = runs[run]
    plt.plot(x, y, alpha=0.5)

# vertical lines
plt.axvline(N/2, color='red', linestyle='--', label='m = n/2')
plt.axvline(2*N, color='green', linestyle='--', label='m = 2n')

# connectivity lines
for run in connected_points:
    plt.axvline(connected_points[run], color='purple', alpha=0.2)

plt.xlabel("Number of Edges (m)")
plt.ylabel("Largest Component Size")

plt.title("Phase Transition (Multiple Runs)")

plt.legend()
plt.grid()

plt.show()
