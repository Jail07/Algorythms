n = int(input())
a = [int(i) for i in input().split()]
c = 0
m = 0
for i in range(len(a)):
    c += a[i]
    if c < 0:
        m += abs(c)
        c = 0
print(m)