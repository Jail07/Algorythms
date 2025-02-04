count = int(input())

records = []
for _ in range(count):
    di, si = map(str, input().split())
    records.append((int(di), si))
min_w = 1
max_w = 2 * 10 ** 9

for di, si in records:
    if si == 'G':
        min_w = max(min_w, di)
    elif si == 'Y':
        min_w = max(min_w, (di + 1) // 2)
        max_w = min(max_w, di - 1)
    elif si == 'R':
        min_w = max(min_w, (di + 2) // 3)
        max_w = min(max_w, (di - 1) // 2)
    elif si == 'B':
        max_w = min(max_w, (di - 1) // 3)

if min_w > max_w:
    print(-1)
else:
    print(min_w, max_w)

