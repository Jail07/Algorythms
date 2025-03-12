import sys
from collections import deque


def main():
    n = int(input())
    if n % 2 == 1:
        print(-1)
        return

    a = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        a[u].append(v)
        a[v].append(u)

    result = 0
    size = [1] * (n + 1)
    visited = [False] * (n + 1)
    stack = [(1, -1)]

    while stack:
        u, parent = stack.pop()
        if not visited[u]:
            visited[u] = True
            stack.append((u, parent))
            for v in a[u]:
                if v != parent:
                    stack.append((v, u))
        else:
            for v in a[u]:
                if v != parent:
                    size[u] += size[v]
            if size[u] % 2 == 0:
                result += 1

    print(result - 1)


if __name__ == "__main__":
    main()