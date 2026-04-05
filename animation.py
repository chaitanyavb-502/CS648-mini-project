import matplotlib
matplotlib.use('Agg')

import networkx as nx
import matplotlib.pyplot as plt
import random
import math
from matplotlib.animation import FuncAnimation

n = 50
edges_per_frame = 1
fps = 10

interval = int(100 / 0.15)   # slow animation

pause_seconds = 5
pause_frames = fps * pause_seconds

G = nx.Graph()
G.add_nodes_from(range(n))

all_edges = [(i, j) for i in range(n) for j in range(i+1, n)]
random.shuffle(all_edges)

pos = nx.spring_layout(G, seed=42)

fig = plt.figure(figsize=(10, 6))

ax_graph = fig.add_axes([0.05, 0.1, 0.6, 0.8])
ax_text = fig.add_axes([0.7, 0.1, 0.25, 0.8])
ax_text.axis('off')

def get_components(G):
    return list(nx.connected_components(G))

def get_colors(G):
    comps = get_components(G)
    color_map = {}
    for i, comp in enumerate(comps):
        for node in comp:
            color_map[node] = i
    return [color_map[node] for node in G.nodes()]

def largest_component_size(G):
    comps = get_components(G)
    if len(comps) == 0:
        return 0
    return max(len(c) for c in comps)

m_half = int(n / 2)
m_2n = int(2 * n)
m_nlogn = int(n * math.log(n))

pause_edges_targets = {m_half, m_2n, m_nlogn}
pause_triggered = set()

pause_counter = 0
footnote_text = ""

# Stop flag
stop_growth = False

edge_index = 0

def update(frame):
    global edge_index, pause_counter, footnote_text, stop_growth

    ax_graph.clear()
    ax_text.clear()
    ax_text.axis('off')

    if pause_counter > 0:
        pause_counter -= 1
    elif not stop_growth:
        for _ in range(edges_per_frame):
            if edge_index < len(all_edges):
                G.add_edge(*all_edges[edge_index])
                edge_index += 1

    # Draw graph
    colors = get_colors(G)
    nx.draw(G, pos,
            node_color=colors,
            node_size=120,
            edge_color='gray',
            with_labels=False,
            ax=ax_graph)

    num_edges = G.number_of_edges()
    giant_size = largest_component_size(G)

    if num_edges == m_half and "half" not in pause_triggered:
        pause_triggered.add("half")
        pause_counter = pause_frames
        footnote_text = "m = n/2"

    elif num_edges == m_2n and "2n" not in pause_triggered:
        pause_triggered.add("2n")
        pause_counter = pause_frames
        footnote_text = "m = 2n"

    elif num_edges == m_nlogn and "nlogn" not in pause_triggered:
        pause_triggered.add("nlogn")
        pause_counter = pause_frames
        c = num_edges / (n * math.log(n))
        footnote_text = f"m = c·n·log n, c = {c:.2f}"

    if giant_size == n and "connected" not in pause_triggered:
        pause_triggered.add("connected")
        pause_counter = pause_frames
        footnote_text = "Graph is connected"
        stop_growth = True

    ax_text.text(0.1, 0.7, f"Edges:\n{num_edges}", fontsize=16)
    ax_text.text(0.1, 0.5, f"Giant Component:\n{giant_size}", fontsize=16)
    ax_text.text(0.1, 0.3, f"Total Nodes:\n{n}", fontsize=16)

    if pause_counter > 0:
        ax_graph.text(0.5, -0.1, footnote_text,
                      transform=ax_graph.transAxes,
                      fontsize=14,
                      ha='center')

    print(f"Frame {frame}, Edges: {num_edges}, Giant: {giant_size}")

frames = 700

anim = FuncAnimation(fig, update, frames=frames, interval=interval)

anim.save("graph_phase_transition.mp4", fps=fps)

print("Video saved as graph_phase_transition.mp4")
