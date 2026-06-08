# Fenwick Tree / Binary Indexed Tree (BIT)
# Supports:
# 1. Point Update
# 2. Prefix Sum Query
#
# Time Complexity:
# update  -> O(log n)
# query   -> O(log n)


class FenwickTree:

    def __init__(self, n):

        self.n = n

        # BIT is usually 1-indexed
        self.bit = [0] * (n + 1)

    # add "delta" at index "idx"
    def update(self, idx, delta):

        # convert to 1-based indexing
        idx += 1

        while idx <= self.n:

            self.bit[idx] += delta

            # move to next responsible node
            idx += idx & -idx

    # returns prefix sum from [0 ... idx]
    def query(self, idx):

        # convert to 1-based indexing
        idx += 1

        res = 0

        while idx > 0:

            res += self.bit[idx]

            # move to parent
            idx -= idx & -idx

        return res

    # returns sum of range [l ... r]
    def range_sum(self, l, r):

        if l > r:
            return 0

        return self.query(r) - self.query(l - 1)


# ---------------- Example ----------------

nums = [1, 2, 3, 4, 5]

n = len(nums)

ft = FenwickTree(n)

# build tree
for i in range(n):
    ft.update(i, nums[i])

# prefix sum [0...3]
print(ft.query(3))       # 1+2+3+4 = 10

# range sum [1...3]
print(ft.range_sum(1, 3)) # 2+3+4 = 9

# add +5 at index 2
ft.update(2, 5)

print(ft.range_sum(1, 3)) # 2+8+4 = 14
