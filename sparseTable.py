# Sparse Table Template
# Used for:
# 1. Range Minimum Query (RMQ)
# 2. Range Maximum Query
# 3. GCD queries
#
# Works only for IMMUTABLE arrays
#
# Query Time  -> O(1)
# Build Time  -> O(n log n)


import math


class SparseTable:

    def __init__(self, nums):

        self.nums = nums
        self.n = len(nums)

        # max power needed
        self.LOG = self.n.bit_length()

        # st[k][i]
        # stores answer for range of length 2^k starting at i
        self.st = [[0] * self.n for _ in range(self.LOG)]

        # level 0 -> original array
        for i in range(self.n):
            self.st[0][i] = nums[i]

        # build sparse table
        for k in range(1, self.LOG):

            length = 1 << k

            half = length >> 1

            for i in range(self.n - length + 1):

                # combine two halves
                self.st[k][i] = min(
                    self.st[k - 1][i],
                    self.st[k - 1][i + half]
                )

    # minimum in range [l ... r]
    def query(self, l, r):

        length = r - l + 1

        # largest power of 2 <= length
        k = length.bit_length() - 1

        # take two overlapping blocks
        return min(
            self.st[k][l],
            self.st[k][r - (1 << k) + 1]
        )


# ---------------- Example ----------------

nums = [5, 2, 4, 7, 1, 3, 6]

sp = SparseTable(nums)

# minimum from index 1 to 4
print(sp.query(1, 4))   # 1

# minimum from index 2 to 6
print(sp.query(2, 6))   # 1

#shorter and better.

class SparseTable:
    def __init__(self, nums, func):
        self.func = func
        self.n = len(nums)
        self.LOG = self.n.bit_length()
        self.st = [[0] * self.n for _ in range(self.LOG)]
        for i in range(self.n):
            self.st[0][i] = nums[i]
        for j in range(1, self.LOG):
            length = 1 << j
            half = 1 << (j - 1)
            for i in range(self.n - length + 1):

                self.st[j][i] = func(
                    self.st[j - 1][i],
                    self.st[j - 1][i + half]
                )
    def query(self, left, right):
        if left > right:
            return None
        length = right - left + 1
        j = length.bit_length() - 1
        return self.func(
            self.st[j][left],
            self.st[j][right - (1 << j) + 1]
        )
