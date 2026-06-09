class RollingHash:

    def __init__(self, nums, base=911382323, mod=10**9 + 7):

        self.nums = nums
        self.n = len(nums)

        self.B = base
        self.MOD = mod

        # prefix hashes
        self.HASH = [0] * self.n

        # powers of base
        self.POWER = [1] * self.n

        # first hash
        self.HASH[0] = nums[0] % mod

        # precompute powers
        for i in range(1, self.n):
            self.POWER[i] = (self.POWER[i - 1] * self.B) % self.MOD

        # build prefix hash array
        for i in range(1, self.n):
            self.HASH[i] = (
                (self.HASH[i - 1] * self.B) + nums[i]
            ) % self.MOD

    # returns hash of nums[l...r]
    def get_hash(self, l, r):

        current = self.HASH[r]

        # remove prefix contribution
        if l > 0:
            current = (
                current
                - self.HASH[l - 1] * self.POWER[r - l + 1]
            ) % self.MOD

        return current % self.MOD

    # checks if any subarray of size k appears exactly once
    def has_unique_subarray(self, k):

        freq = {}

        for i in range(self.n - k + 1):

            j = i + k - 1

            h = self.get_hash(i, j)

            freq[h] = freq.get(h, 0) + 1

        # check if any hash frequency is 1
        for h in freq:
            if freq[h] == 1:
                return True

        return False


# ---------------- Example Usage ----------------

nums = [1, 2, 3, 4, 2, 3]

rh = RollingHash(nums)

# hash of subarray [2,3,4]
print(rh.get_hash(1, 3))

# check unique subarray of length 2
print(rh.has_unique_subarray(2))
