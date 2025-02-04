def solve():
    import sys
    input = sys.stdin.read
    data = input().split()

    idx = 0
    t = int(data[idx])
    idx += 1

    for _ in range(t):
        n = int(data[idx])
        idx += 1
        a = list(map(int, data[idx:idx + n]))
        idx += n
        b = list(map(int, data[idx:idx + n]))
        idx += n
        diff = [a[i] - b[i] for i in range(n)]
        max_diff = max(diff)

        result = [i + 1 for i in range(n) if diff[i] == max_diff]

        print(len(result))
        print(" ".join(map(str, result)))


if __name__ == "__main__":
    solve()