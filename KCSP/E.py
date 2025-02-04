import sys


def can_prepare(z, ingredients):
    left, right = 0, z  
    while left <= right:
        x = (left + right) // 2
        y = z - x
        if all(x * ai + y * bi <= ti for ti, ai, bi in ingredients):
            return True
        right = x - 1
    return False


def max_breakfasts(n, ingredients):
    left, right = 0, 10 ** 6
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if can_prepare(mid, ingredients):
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result


def main():
    input = sys.stdin.read
    data = input().split()

    n = int(data[0])
    ingredients = []
    index = 1
    for _ in range(n):
        ti, ai, bi = map(int, data[index:index + 3])
        ingredients.append((ti, ai, bi))
        index += 3

    print(max_breakfasts(n, ingredients))


if __name__ == "__main__":
    main()
