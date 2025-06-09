import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вершин (зупинки автобуса №61)
stops = [
    "Löbtau, Tharandter Straße",
    "Cotta, Gottfried-Keller-Straße",
    "Altcotta",
    "Freital, Deuben",
    "Freital, Potschappel"
]
G.add_nodes_from(stops)

# Додавання ребер (послідовні зв’язки між зупинками)
edges = [
    ("Löbtau, Tharandter Straße", "Cotta, Gottfried-Keller-Straße"),
    ("Cotta, Gottfried-Keller-Straße", "Altcotta"),
    ("Altcotta", "Freital, Deuben"),
    ("Freital, Deuben", "Freital, Potschappel")
]
G.add_edges_from(edges)

# Візуалізація графа
pos = nx.spring_layout(G)
plt.figure(figsize=(10, 6))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=8, font_weight='bold')
plt.title("Маршрут автобуса №61 у Дрездені")
plt.show()

# Аналіз характеристик
print("Кількість вершин:", G.number_of_nodes())
print("Кількість ребер:", G.number_of_edges())
print("Ступінь вершин:", dict(G.degree()))

# task2

stops = [
    "Löbtau, Tharandter Straße",
    "Cotta, Gottfried-Keller-Straße",
    "Altcotta",
    "Freital, Deuben",
    "Freital, Potschappel"
]
G.add_nodes_from(stops)
edges = [
    ("Löbtau, Tharandter Straße", "Cotta, Gottfried-Keller-Straße"),
    ("Cotta, Gottfried-Keller-Straße", "Altcotta"),
    ("Altcotta", "Freital, Deuben"),
    ("Freital, Deuben", "Freital, Potschappel")
]
G.add_edges_from(edges)

# Define source and target stops
source = "Löbtau, Tharandter Straße"
target = "Freital, Potschappel"

# BFS path (using nx.shortest_path, which defaults to BFS for unweighted graphs)
bfs_path = nx.shortest_path(G, source=source, target=target)
print("BFS path:", bfs_path)
print("BFS path length (edges):", len(bfs_path) - 1)

# Custom DFS pathfinding function
def dfs_path(graph, start, goal, path=None, visited=None):
    if path is None:
        path = [start]
    if visited is None:
        visited = set()
    visited.add(start)
    
    if start == goal:
        return path
    
    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            new_path = dfs_path(graph, neighbor, goal, path + [neighbor], visited.copy())
            if new_path:
                return new_path
    return None

# DFS path
dfs_path = dfs_path(G, source, target)
print("DFS path:", dfs_path)
print("DFS path length (edges):", len(dfs_path) - 1)

# Comparison
print("\nComparison:")
if dfs_path == bfs_path:
    print("DFS and BFS paths are identical because the graph is linear.")
else:
    print("DFS and BFS paths differ. DFS may explore deeper paths, while BFS guarantees the shortest path.")

# task3

# Створення графа з вагами
G_weighted = nx.Graph()
weighted_edges = [
    ("Löbtau, Tharandter Straße", "Cotta, Gottfried-Keller-Straße", 1.5),
    ("Cotta, Gottfried-Keller-Straße", "Altcotta", 2.0),
    ("Altcotta", "Freital, Deuben", 3.0),
    ("Freital, Deuben", "Freital, Potschappel", 1.0)
]
G_weighted.add_weighted_edges_from(weighted_edges)

# Алгоритм Дейкстри для однієї пари
source = "Löbtau, Tharandter Straße"
target = "Freital, Potschappel"
dijkstra_path = nx.dijkstra_path(G_weighted, source, target, weight='weight')
dijkstra_length = nx.dijkstra_path_length(G_weighted, source, target, weight='weight')
print("Шлях за Дейкстрою:", dijkstra_path)
print("Довжина шляху (км):", dijkstra_length)

# Шляхи між усіма парами вершин
all_paths = dict(nx.all_pairs_dijkstra_path(G_weighted, weight='weight'))
all_lengths = dict(nx.all_pairs_dijkstra_path_length(G_weighted, weight='weight'))
print("\nШляхи між усіма вершинами:")
for node, paths in all_paths.items():
    print(f"Від {node}: {paths}")
print("\nДовжини шляхів (км):")
for node, lengths in all_lengths.items():
    print(f"Від {node}: {lengths}")
