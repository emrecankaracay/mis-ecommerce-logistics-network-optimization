import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "data" / "network_data.csv"
RESULTS_DIR = BASE_DIR / "results"
RESULTS_DIR.mkdir(exist_ok=True)

SOURCE_NODE = "Warehouse"
TARGET_NODE = "CustomerZone"


def load_data():
    return pd.read_csv(DATA_PATH)


def build_graph(df):
    G = nx.Graph()

    for _, row in df.iterrows():
        G.add_edge(
            row["source"],
            row["target"],
            distance=float(row["distance_km"]),
            time=float(row["delivery_time_min"])
        )

    return G


def solve_shortest_path(G):
    path = nx.shortest_path(
        G,
        source=SOURCE_NODE,
        target=TARGET_NODE,
        weight="distance"
    )

    total_distance = nx.shortest_path_length(
        G,
        source=SOURCE_NODE,
        target=TARGET_NODE,
        weight="distance"
    )

    total_time = 0
    for i in range(len(path) - 1):
        total_time += G[path[i]][path[i + 1]]["time"]

    return path, total_distance, total_time


def save_results(path, total_distance, total_time):
    output_file = RESULTS_DIR / "solution_output.txt"

    text = f"""
Shortest Delivery Route Optimization Result

Selected Optimization Model: Shortest Path Problem
Algorithm: Dijkstra Algorithm implemented in NetworkX

Source Node: {SOURCE_NODE}
Target Node: {TARGET_NODE}

Shortest Path:
{" -> ".join(path)}

Total Distance: {total_distance:.2f} km
Estimated Delivery Time: {total_time:.2f} minutes

Managerial Interpretation:
The result identifies the shortest delivery route from the warehouse to the customer zone.
This helps an e-commerce company reduce delivery distance, improve logistics planning,
and support faster order fulfillment.
"""

    output_file.write_text(text.strip(), encoding="utf-8")
    print(text)


def visualize(G, path):
    plt.figure(figsize=(15, 9))

    pos = {
        "Warehouse": (0, 0),
        "DistributionCenter_A": (2.5, 2.7),
        "DistributionCenter_B": (2.5, -2.7),
        "DistributionCenter_C": (2.5, 0),
        "Hub_D": (5.5, 2.2),
        "Hub_E": (5.5, 0),
        "Hub_F": (5.5, -2.2),
        "CustomerZone": (8.5, 0),
    }

    path_edges = list(zip(path, path[1:]))

    other_edges = [
        edge for edge in G.edges()
        if edge not in path_edges and (edge[1], edge[0]) not in path_edges
    ]

    nx.draw_networkx_nodes(
        G,
        pos,
        node_size=2700,
        node_color="lightblue",
        edgecolors="black",
        linewidths=1.2
    )

    nx.draw_networkx_labels(
        G,
        pos,
        font_size=9,
        font_weight="bold"
    )

    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=other_edges,
        width=1.4,
        edge_color="gray"
    )

    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=path_edges,
        width=3.5,
        edge_color="red"
    )

    label_positions = {
        ("Warehouse", "DistributionCenter_A"): (1.25, 1.55),
        ("Warehouse", "DistributionCenter_B"): (1.25, -1.55),
        ("Warehouse", "DistributionCenter_C"): (1.15, 0.25),
        ("DistributionCenter_A", "Hub_D"): (4.0, 2.7),
        ("DistributionCenter_A", "Hub_E"): (4.0, 1.5),
        ("DistributionCenter_B", "Hub_D"): (4.0, -0.3),
        ("DistributionCenter_B", "Hub_F"): (4.0, -2.7),
        ("DistributionCenter_C", "Hub_E"): (4.0, 0.35),
        ("DistributionCenter_C", "Hub_F"): (4.0, -1.25),
        ("Hub_D", "CustomerZone"): (7.0, 1.55),
        ("Hub_E", "CustomerZone"): (7.0, 0.35),
        ("Hub_F", "CustomerZone"): (7.0, -1.35),
        ("Hub_D", "Hub_E"): (5.85, 1.15),
    }

    for u, v, data in G.edges(data=True):
        key = (u, v)
        reverse_key = (v, u)

        x, y = label_positions.get(
            key,
            label_positions.get(
                reverse_key,
                ((pos[u][0] + pos[v][0]) / 2, (pos[u][1] + pos[v][1]) / 2)
            )
        )

        plt.text(
            x,
            y,
            f"{data['distance']:.0f} km",
            fontsize=9,
            ha="center",
            va="center",
            bbox=dict(
                facecolor="white",
                edgecolor="gray",
                boxstyle="round,pad=0.2",
                alpha=0.9
            )
        )

    plt.title(
        "Shortest Delivery Route Optimization in an E-commerce Logistics Network",
        fontsize=14,
        fontweight="bold"
    )

    plt.text(
        0,
        -3.55,
        "Red edges show the shortest delivery route. Edge labels show distance in kilometers.",
        fontsize=10
    )

    plt.axis("off")
    plt.tight_layout()

    plt.savefig(RESULTS_DIR / "network_visualization.png", dpi=300)
    plt.close()


def main():
    df = load_data()
    G = build_graph(df)

    path, total_distance, total_time = solve_shortest_path(G)

    save_results(path, total_distance, total_time)
    visualize(G, path)


if __name__ == "__main__":
    main()