import sys


def next_moon_phase(sx, sy, mx, my):
    P = mx * sx + my * sy
    C = mx * sy - my * sx

    if P > 0:
        return "Full moon" if C > 0 else "Third quarter"
    else:
        return "First quarter" if C > 0 else "New moon"


def main():
    q = int(input())
    input_data = []
    for i in range(q):
        input_data.append(list(map(int, input().split())))

    results = []

    for i in input_data:
        sx, sy, mx, my = i
        results.append(next_moon_phase(sx, sy, mx, my))

    sys.stdout.write("\n".join(results) + "\n")


if __name__ == "__main__":
    main()
