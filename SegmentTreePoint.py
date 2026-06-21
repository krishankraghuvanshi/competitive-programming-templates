class SegmentTree:
	"""
		Remember to change the func content as well as the initializer to display the content
	"""
	@staticmethod
	def func(a, b):
		# Change this function depending upon needs
		return max(a, b)
	def __init__(self, data):
		self.n = len(data)
		self.tree = [0] * (self.n<<1)
		self.build(data)
	def build(self, data):
		for i in range(self.n):
			self.tree[self.n + i] = data[i]
		for i in range(self.n - 1, 0, -1):
			self.tree[i] = self.func(self.tree[i<<1], self.tree[(i<<1) + 1])
	def update(self, pos, value):
		# Update the value at the leaf node
		pos += self.n
		# For updating
		self.tree[pos] = value
		# self.tree[pos] += value
		# If you want to add rather than update
		while pos > 1:
			pos >>= 1
			self.tree[pos] = self.func(self.tree[pos<<1], self.tree[(pos<<1) + 1])
	def query(self, left, right):
		# Query the maximum value in the range [left, right)
		left += self.n
		right += self.n
		# Change the initializer depending upon the self.func
		max_val = float('-inf')
		##
		while left < right:
			if left&1:
				max_val = self.func(max_val, self.tree[left])
				left += 1
			if right&1:
				right -= 1
				max_val = self.func(max_val, self.tree[right])
			left >>= 1
			right >>= 1
		return max_val
	def __repr__(self):
		values = [str(self.query(i, i + 1)) for i in range(self.n)]
		return f"Seg[{', '.join(values)}]"
''''''

class SegmentTree:
    def __init__(self, nums):
        self.nums = nums
        self.N = len(nums)
        self.tree = [0] * (4*self.N+1)
        self.pref_max = [0] * (4*self.N+1)
        self.build(0, 0, self.N-1, self.nums)
 
    def merge(self, index):
        L = 2*index+1
        R = 2*index+2
        self.tree[index] = self.tree[L]+self.tree[R]
        self.pref_max[index] = max(self.pref_max[L], self.tree[L]+self.pref_max[R])  
 
    def build(self, index, left, right, nums):
        if left == right:
            self.tree[index] = nums[left]
            self.pref_max[index] = max(0, nums[left])
            return
        mid = (left+right) // 2
        self.build(2*index+1, left, mid, nums)
        self.build(2*index+2, mid+1, right, nums)
        self.merge(index)    
 
    def update(self, index, left, right, pos, value):
        if left == right:
            self.tree[index] = value
            self.pref_max[index] = max(0, value)
            return
        mid = (left+right) // 2
        if pos <= mid:
            self.update(2*index+1, left, mid, pos, value)
        else:
            self.update(2*index+2, mid+1, right, pos, value)
        self.merge(index)
 
    def query(self, index, left, right, q_left, q_right):
        if left > q_right or right < q_left:
            return None
        if q_left <= left and right <= q_right:
            return self.tree[index], self.pref_max[index]
        mid = (left+right) // 2 
        L_res = self.query(2*index+1, left, mid, q_left, q_right)
        R_res = self.query(2*index+2, mid+1, right, q_left, q_right)
        if L_res is None:
            return R_res
        if R_res is None:
            return L_res
        L_sum, L_pref = L_res
        R_sum, R_pref = R_res
 
        merge_sum = L_sum+R_sum
        return (merge_sum, max(L_pref, L_sum+R_pref))   
