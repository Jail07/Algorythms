def main(x):
    max_b = x // 111
    for b in range(1 + max_b):
        a = x - 111 * b
        if a % 11 == 0:
            return True
    return False


t = int(input())
for _ in range(t):
    x = int(input())
    if main(x):
        print("YES")
    else:
        print("NO")