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

        assigned = [False] * (n + 1)
        unassigned_princess = -1

        for princess in range(1, n + 1):
            k = int(data[idx])
            idx += 1
            princes = list(map(int, data[idx:idx + k]))
            idx += k

            found = False
            for prince in princes:
                if not assigned[prince]:
                    assigned[prince] = True
                    found = True
                    break

            if not found:
                unassigned_princess = princess

        if unassigned_princess == -1:
            print("OPTIMAL")
        else:
            unassigned_prince = -1
            for prince in range(1, n + 1):
                if not assigned[prince]:
                    unassigned_prince = prince
                    break

            print("IMPROVE")
            print(unassigned_princess, unassigned_prince)


if __name__ == "__main__":
    solve()