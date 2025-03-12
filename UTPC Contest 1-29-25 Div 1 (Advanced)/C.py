def main():
    n, k = map(int, input().split())
    dragon = list(map(int, input().split()))
    results = []
    result = 0
    for i in range(len(dragon)):
        if i < len(dragon) - 1:
            diff = abs(dragon[i] - dragon[i+1])
            if diff <= k:
                result += 1
            else:
                result += 1
                results.append(result)
                result = 0
        else:
            result += 1
            results.append(result)
            print(sorted(results)[-1])

main()