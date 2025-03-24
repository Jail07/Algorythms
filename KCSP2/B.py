n, d = map(int, input().split())
v = list(map(int, input().split()))
v.sort(reverse=True)

clusters = 0
i = 0
while i < n:
    clusters += 1
    leader = v[i]
    i += 1
    while i < n and (v[i] >= leader - 2*d and v[i] <= leader):
        i += 1

print(clusters)