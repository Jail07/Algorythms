count = input().split()
a = list(map(int, input().split()))
b = list(map(int, input().split()))
max_b = -1
for i in range(int(count[0])):
    try:
        if a[i]+b[i] > int(count[1]) and a[i+1]+b[i+1] > int(count[1]):
            max_b = max(max_b, b[i+1])
    except IndexError:
        pass

if max_b == -1:
    print(-1)
else:
    print(max_b)

