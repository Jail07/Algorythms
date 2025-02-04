n = int(input())
a = [int(i) for i in input().split()]
l = [[] for i in range(n)]
T = 0

for i in range(n):
    l[i] = [int(i) for i in input().split()]

for i in range(n):
    T += a[i]
    r = l[i][0]
    g = l[i][1]
    d = l[i][2]
    c = r + g
    h = (T + d) % c
    if h >= g:
        T += c - h
print(T)