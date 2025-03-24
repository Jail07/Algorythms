n, d = map(int, input().split())
v = list(map(int, input().split()))
v.sort()

clusters = 0
i = 0
while i < n:
    clusters += 1
    leader = v[i]
    while i < n and v[i] <= leader + 2 * d:
        i += 1

print(clusters)