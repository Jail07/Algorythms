def decompress(C):
    n = len(C)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(n):
        if dp[i] == float('inf'):
            continue

        if C[i] == '0' or C[i] == '1':
            if dp[i + 1] > dp[i] + 1:
                dp[i + 1] = dp[i] + 1

        if C[i] != '0':
            num = 0
            for j in range(i, min(i + 10, n)):
                num = num * 10 + int(C[j])
                if num > 10**9:
                    break
                if dp[j + 1] > dp[i] + len(str(num)) + 1:
                    dp[j + 1] = dp[i] + len(str(num)) + 1

    result = []
    current = n
    while current > 0:
        if C[current - 1] == '0' or C[current - 1] == '1':
            result.append(C[current - 1])
            current -= 1
        else:
            for j in range(max(0, current - 10), current):
                num = int(C[j:current])
                if dp[current] == dp[j] + len(str(num)) + 1:
                    result.append(str(num))
                    current = j
                    break

    result.reverse()
    return dp[n], ' '.join(result)

C = input().strip()
length, decompressed = decompress(C)
print(length)
print(decompressed)