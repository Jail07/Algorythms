def main():
    t = int(input())
    a = list(map(int, input().split()))
    print(a)
    string = ""
    for j in range(t):
        if j % 2 == 0:
            string += "(" * a[j]
        else:
            string += ")" * a[j]
    print(string)


main()
