import matplotlib
matplotlib.use('TkAgg')  # Используем TkAgg бэкенд
import matplotlib.pyplot as plt
import networkx as nx

# Функция для добавления вершин и рёбер
def build_graph():
    G = nx.DiGraph()

    # Ввод количества вершин
    num_vertices = int(input("Введите количество вершин: "))
    for i in range(1, num_vertices + 1):
        G.add_node(i)

    # Ввод рёбер
    num_edges = int(input("Введите количество рёбер: "))
    for _ in range(num_edges):
        u, v, weight = map(int, input("Введите ребро (начало, конец, вес): ").split())
        G.add_edge(u, v, weight=weight)

    return G

# Функция для отрисовки графа
def draw_graph(graph):
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold', edge_color='gray')
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    plt.title("Graph Visualization")
    plt.show()

# Алгоритм Дейкстры
def dijkstra(graph, start):
    shortest_paths = {start: (None, 0)}  # {вершина: (предыдущая вершина, расстояние)}
    current_node = start
    visited = set()

    while current_node is not None:
        visited.add(current_node)
        destinations = graph[current_node]  # Соседи текущей вершины
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node, edge_data in destinations.items():
            weight = edge_data['weight'] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)

        # Выбор следующей вершины
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            break

        # Переход к следующей вершине с минимальным расстоянием
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    return shortest_paths

# Основная программа
if __name__ == "__main__":
    # Построение графа
    G = build_graph()

    # Визуализация графа
    draw_graph(G)

    # Применение алгоритма Дейкстры
    start_node = int(input("Введите начальную вершину для алгоритма Дейкстры: "))
    shortest_paths = dijkstra(G, start_node)

    # Вывод результатов
    print("Кратчайшие пути от вершины", start_node)
    for node, (prev_node, distance) in shortest_paths.items():
        print(f"Вершина {node}: расстояние = {distance}, предыдущая вершина = {prev_node}")