import heapq

def find_max_capacity(n, roads, s, t):
    graph = [[] for _ in range(n + 1)]
    for a, b, w in roads:
        graph[a].append((b, w))

    capacity = [0] * (n + 1)
    capacity[s] = float('inf')
    heap = [(-capacity[s], s)]  # Максимизируем минимальную пропускную способность

    while heap:
        current_cap, u = heapq.heappop(heap)
        current_cap = -current_cap

        if u == t:
            return current_cap

        for v, w in graph[u]:
            new_cap = min(current_cap, w)
            if new_cap > capacity[v]:
                capacity[v] = new_cap
                heapq.heappush(heap, (-new_cap, v))

    return -1  # Если путь не найден

# Ввод данных
n, m = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(m)]
s, t = map(int, input().split())

# Вывод результата
print(find_max_capacity(n, roads, s, t))