def pass_r(a, m, c, k):
    while m < len(a):
        if a[m]:
            if m+1 in k:
                a[m] = not a[m]
            pass_r(a, m+1, c+1, k)
        else:
            a[m] = not a[m]
            pass_r(a, 0, c+1, k)
    print(c)

n, k = input().split()
n, k = int(n), int(k)
r = [True] * n
ks = [int(i) for i in input().split()]
for el in ks:
    r[el-1] = False
c = 0

m = 0
while m < len(r):
    if r[m]:
        if m+1 in ks:
            r[m] = not r[m]
        m += 1
    else:
        r[m] = not r[m]
        m = 0
    c += 1
print(c)