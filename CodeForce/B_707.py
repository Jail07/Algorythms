def main():
    n, m, k = map(int, input().split())
    roads = []

    for i in range(m):
        u, v, l = map(int, input().split())
        roads.append([u, v, l])

    data = list(map(int, input().split()))
    min_d = float('inf')

    for u, v, l in roads:
        if (u in data and v not in data) or (v in data and u not in data):
            min_d = min(min_d, l)

    if min_d != float('inf'):
        print(min_d)
    else:
        print(-1)


if __name__ == '__main__':
    main()
