import networkx as nx
from collections import deque
import heapq
import matplotlib.pyplot as plt

# Завдання 1: Створення та аналіз графа
# Створення графа маршруту автобуса №61
G = nx.Graph()
stops = [
    "Löbtau, Tharandter Straße",
    "Cotta, Gottfried-Keller-Straße",
    "Altcotta",
    "Freital, Deuben",
    "Freital, Potschappel"
]
G.add_nodes_from(stops)
edges = [
    ("Löbtau, Tharandter Straße", "Cotta, Gottfried-Keller-Straße", {'weight': 1.5}),
    ("Cotta, Gottfried-Keller-Straße", "Altcotta", {'weight': 2.0}),
    ("Altcotta", "Freital, Deuben", {'weight': 3.0}),
    ("Freital, Deuben", "Freital, Potschappel", {'weight': 1.0})
]
G.add_edges_from(edges)

# Візуалізація графа
pos = nx.spring_layout(G)
plt.figure(figsize=(10, 6))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=8, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})
plt.title("Маршрут автобуса №61 у Дрездені")
plt.savefig("bus61_graph.png")
plt.close()

# Аналіз характеристик
print("Завдання 1: Аналіз графа")
print("Кількість вершин:", G.number_of_nodes())
print("Кількість ребер:", G.number_of_edges())
print("Ступінь вершин:", dict(G.degree()))

# Завдання 2: Власна реалізація BFS
def bfs_path(graph, start, goal):
    queue = deque([(start, [start])])
    visited = {start}
    
    while queue:
        (vertex, path) = queue.popleft()
        for neighbor in graph.neighbors(vertex):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor]
                if neighbor == goal:
                    return new_path
                queue.append((neighbor, new_path))
    return None

# Завдання 2: Власна реалізація DFS
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

# Завдання 3: Власна реалізація алгоритму Дейкстри
def dijkstra_path(graph, start, goal):
    distances = {node: float('infinity') for node in graph.nodes()}
    distances[start] = 0
    previous = {node: None for node in graph.nodes()}
    pq = [(0, start)]
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
        if current_vertex == goal:
            path = []
            while current_vertex is not None:
                path.append(current_vertex)
                current_vertex = previous[current_vertex]
            return path[::-1], current_distance
        
        if current_distance > distances[current_vertex]:
            continue
            
        for neighbor in graph.neighbors(current_vertex):
            weight = graph[current_vertex][neighbor].get('weight', 1)
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))
    
    return None, float('infinity')

# Виконання завдання 2
source = "Löbtau, Tharandter Straße"
target = "Freital, Potschappel"

print("\nЗавдання 2: Порівняння DFS і BFS")
bfs_path_result = bfs_path(G, source, target)
print("BFS шлях:", bfs_path_result)
print("Довжина BFS шляху (ребер):", len(bfs_path_result) - 1)

dfs_path_result = dfs_path(G, source, target)
print("DFS шлях:", dfs_path_result)
print("Довжина DFS шляху (ребер):", len(dfs_path_result) - 1)

# Порівняння
print("\nПорівняння:")
if dfs_path_result == bfs_path_result:
    print("Шляхи DFS і BFS однакові, оскільки граф є лінійним.")
else:
    print("Шляхи DFS і BFS відрізняються. DFS може досліджувати глибші гілки, тоді як BFS гарантує найкоротший шлях.")

# Виконання завдання 3
print("\nЗавдання 3: Алгоритм Дейкстри")
dijkstra_path_result, dijkstra_length = dijkstra_path(G, source, target)
print("Шлях за Дейкстрою:", dijkstra_path_result)
print("Довжина шляху (км):", dijkstra_length)
