MOD = 10 ** 9 + 7
MAX_K = 10 ** 5

fact = [1] * (MAX_K + 1)
inv_fact = [1] * (MAX_K + 1)


def precompute():
    for i in range(2, MAX_K + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact[MAX_K] = pow(fact[MAX_K], MOD - 2, MOD)
    for i in range(MAX_K - 1, 0, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD


def binomial_coefficient(n, k):
    if n > k:
        return 0
    return fact[k] * inv_fact[n] % MOD * inv_fact[k - n] % MOD


def main():
    precompute()
    n, m = map(int, input().split())
    k = list(map(int, input().split()))

    result = 1
    for ki in k:
        result = result * binomial_coefficient(n, ki) % MOD

    print(result)


main()
