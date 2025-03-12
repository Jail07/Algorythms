import networkx as nx
import matplotlib.pyplot as plt

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
        u, v = map(int, input("Введите ребро (начало, конец): ").split())
        G.add_edge(u, v)

    return G

# Функция для отрисовки графа
def draw_graph(graph):
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold', edge_color='gray')
    plt.title("Graph Visualization")
    plt.show()

# Основная программа
if __name__ == "__main__":
    # Построение графа
    G = build_graph()

    # Визуализация графа
    draw_graph(G)