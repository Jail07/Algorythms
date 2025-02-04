

a, b = input().split()
a, b = int(a), int(b)
m = [int(i) for i in input().split()]
count = 0
boolean = True
for i in m:
    if abs(m[i] - m[i+1]) >= b:
        count +=1
        count = b
        print(b)
        boolean = False
    elif count != b:
        print(-1)
        boolean = False
