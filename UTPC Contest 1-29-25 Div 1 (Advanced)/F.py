import sys

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.size = 2 ** (self.n - 1).bit_length()
        self.tree = [0] * (2 * self.size)
        for i in range(self.n):
            self.tree[self.size + i] = data[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, idx, value):
        idx += self.size
        self.tree[idx] = value
        idx //= 2
        while idx >= 1:
            new_val = max(self.tree[2 * idx], self.tree[2 * idx + 1])
            if self.tree[idx] == new_val:
                break
            self.tree[idx] = new_val
            idx //= 2

    def get_max(self, l, r):
        l += self.size
        r += self.size
        res = 0
        while l <= r:
            if l % 2 == 1:
                res = max(res, self.tree[l])
                l += 1
            if r % 2 == 0:
                res = max(res, self.tree[r])
                r -= 1
            l //= 2
            r //= 2
        return res

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    n = int(data[idx])
    q = int(data[idx + 1])
    idx += 2
    heights = list(map(int, data[idx:idx + n]))
    idx += n

    st = SegmentTree(heights)

    results = []
    for _ in range(q):
        type_query = int(data[idx])
        if type_query == 1:
            p = int(data[idx + 1]) - 1
            current_height = heights[p]
            max_height = st.get_max(0, n - 1)
            results.append(str(max(0, max_height - current_height)))
            idx += 2
        elif type_query == 2:
            p = int(data[idx + 1]) - 1
            x = int(data[idx + 2])
            heights[p] = x
            st.update(p, x)
            idx += 3

    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()