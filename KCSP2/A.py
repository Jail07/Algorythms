def main(n):
    k = 0
    while (k + 1) * (k + 3) <= n:
        k += 1
    return k

if __name__ == '__main__':
    n = int(input())
    print(main(n))
