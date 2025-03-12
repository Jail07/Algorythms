def hotel_gilbertaburnsa(n, a):
    f = [(i + a[i]) % n for i in range(n)]
    return len(set(f)) == n


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if hotel_gilbertaburnsa(n, a):
        print("YES")
    else:
        print("NO")