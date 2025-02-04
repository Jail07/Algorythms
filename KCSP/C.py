import sys
import bisect

def main():
    input = sys.stdin.read
    data = input().split()

    idx = 0
    n = int(data[idx])
    idx += 1

    p = list(map(int, data[idx:idx + n]))
    idx += n

    m = int(data[idx])
    idx += 1

    s = list(map(int, data[idx:idx + m]))

    tasks = [(p[i], i + 1) for i in range(n)]

    tasks.sort()

    sorted_p = [task[0] for task in tasks]

    result = []
    for sj in s:
        priority = p[sj - 1]

        count = bisect.bisect_right(sorted_p, priority)
        result.append(str(count))

    print(' '.join(result))


if __name__ == "__main__":
    main()