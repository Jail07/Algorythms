import sys
import math

def prime_factors(x):
    pf = []
    i = 2
    while i * i <= x:
        while x % i == 0:
            pf.append(i)
            x //= i
        i += 1
    if x > 1:
        pf.append(x)
    return pf

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        ans = 0
        one = [0] * (n + 1)
        two_same = [0] * (n + 1)
        two_diff = [0] * (n + 1)
        cnt = [0] * (n + 1)
        prime_so_far = 0
        for _ in range(n):
            x = int(data[idx])
            idx += 1
            pf = prime_factors(x)
            if len(pf) > 2:
                continue
            if len(pf) == 1:
                one[x] += 1
                prime_so_far += 1
                ans += two_same[x] + two_diff[x] + (prime_so_far - one[x])
            elif pf[0] == pf[1]:
                two_same[pf[0]] += 1
                ans += one[pf[0]] + two_same[pf[0]]
            else:
                two_diff[pf[0]] += 1
                two_diff[pf[1]] += 1
                cnt[x] += 1
                ans += one[pf[0]] + one[pf[1]] + cnt[x]
        print(ans)

if __name__ == "__main__":
    main()