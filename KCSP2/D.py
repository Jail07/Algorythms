def main():
    import sys
    C = sys.stdin.readline().strip()
    n = len(C)
    inf = float('inf')
    dp = [inf] * (n + 1)
    dp[0] = 0
    prev = [-1] * (n + 1)

    for i in range(n):
        if C[i] not in {'0', '1'}:
            continue
        max_j = max(0, i - 9)
        for j in range(max_j, i):
            num_str = C[j:i]
            if not num_str:
                continue
            if len(num_str) > 1 and num_str[0] == '0':
                continue
            num = int(num_str)
            if num < 1:
                continue
            if dp[j] + num < dp[i + 1]:
                dp[i + 1] = dp[j] + num
                prev[i + 1] = j

    path = []
    current = n
    while current > 0:
        j = prev[current]
        symbol = C[current - 1]
        num_str = C[j:current - 1]
        path.append((num_str, symbol))
        current = j

    path.reverse()
    result = []
    for num_str, symbol in path:
        result.append(num_str)
        result.append(symbol)

    print(dp[n])
    print(' '.join(result))


if __name__ == "__main__":
    main()
