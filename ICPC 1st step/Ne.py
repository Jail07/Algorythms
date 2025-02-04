n, m = input().split()
n, m = int(n), int(m)
a = [int(i) for i in input().split()]
d = [0 for i in range(len(a)-1)]
print(d)

for i in range(len(a)-1):
    d[i] = abs(a[i+1] - a[i])
print(d)

m = max(d)
print(m)
c = 1
for i in range(len(d)):
    for j in range(len(d)):


print(c)