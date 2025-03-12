def main():
    n = int(input())
    s = list(input())
    # s = "bacabcab"
    m = 0
    for ch in range(ord('z'), ord('a') - 1, -1):
        i = 0
        while i < len(s):
            if s[i] == chr(ch):
                if (i > 0 and ord(s[i - 1]) == ch - 1) or (i < len(s) - 1 and ord(s[i + 1]) == ch - 1):
                    del s[i]
                    m += 1
                    i = max(i - 1, 0)
                else:
                    i += 1
            else:
                i += 1

    print(m)


main()