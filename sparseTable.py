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
