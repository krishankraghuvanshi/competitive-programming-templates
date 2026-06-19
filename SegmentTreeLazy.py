class SegmentTree:
	def __init__(self, data, default=0, func=max):
		# don't forget to change func here
		# default is the value given to it byy default
		self._default = default
		self._func = func

		self._len = len(data)
		self._size = _size = 1 << (self._len - 1).bit_length()
		self._lazy = [0] * (2 * _size)

		self.data = [default] * (2 * _size)
		self.data[_size:_size + self._len] = data
		for i in reversed(range(_size)):
			self.data[i] = func(self.data[i + i], self.data[i + i + 1])
	def __len__(self):
		return self._len
	def _push(self, idx):
		q, self._lazy[idx] = self._lazy[idx], 0
		self._lazy[2 * idx] += q
		self._lazy[2 * idx + 1] += q
		self.data[2 * idx] += q
		self.data[2 * idx + 1] += q
	def _update(self, idx):
		for i in reversed(range(1, idx.bit_length())):
			self._push(idx >> i)
	def _build(self, idx):
		idx >>= 1
		while idx:
			self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1]) + self._lazy[idx]
			idx >>= 1
	def add(self, start, stop, value):
		# lazily add value to [start, stop)
		start = start_copy = start + self._size
		stop = stop_copy = stop + self._size
		while start < stop:
			if start & 1:
				self._lazy[start] += value
				self.data[start] += value
				start += 1
			if stop & 1:
				stop -= 1
				self._lazy[stop] += value
				self.data[stop] += value
			start >>= 1
			stop >>= 1
		self._build(start_copy)
		self._build(stop_copy - 1)
	def query(self, start, stop, default=-float('inf')):
		# func of data[start, stop)
		# don't forget to update the default
		start += self._size
		stop += self._size
		self._update(start)
		self._update(stop - 1)
		res = default
		while start < stop:
			if start & 1:
				res = self._func(res, self.data[start])
				start += 1
			if stop & 1:
				stop -= 1
				res = self._func(res, self.data[stop])
			start >>= 1
			stop >>= 1
		return res
	def __repr__(self):
		return "LazySegmentTree({0})".format(self.data)
```---------------------------------------------------```
class SegmentTree:
    def __init__(self, N):
        self.N = N
        self.tree = [0] * (4*N)
        self.lazy = [0] * (4*N)

    def push(self, index, left, right):
        if self.lazy[index] == 0:
            return
        self.tree[index] += (right-left+1) * self.lazy[index]
        if left != right:
            self.lazy[2*index+1] += self.lazy[index]
            self.lazy[2*index+2] += self.lazy[index]
        self.lazy[index] = 0     

    def update(self, index, left, right, pos, value):
        self.push(index, left, right)
        if left == right:
            self.tree[index] += value
            return 
        mid = (left + right) // 2
        if pos <= mid:
            self.update(2*index+1, left, mid, pos, value)
        else:
            self.update(2*index+2, mid+1, right, pos, value)
        self.tree[index] = self.tree[2*index+1]+self.tree[2*index+2]
        
    def range_update(self, index, left, right, q_left, q_right, value):
        self.push(index, left, right)
        if left > q_right or right < q_left:
            return 
        if q_left <= left and right <= q_right:
            self.lazy[index]+=value
            self.push(index, left, right)
            return 
        mid = (left + right) // 2
        self.range_update(2*index+1, left, mid, q_left, q_right, value)
        self.range_update(2*index+2, mid+1, right, q_left, q_right, value)
        self.tree[index] = self.tree[2*index+1]+self.tree[2*index+2]

    def query(self, index, left, right, q_left, q_right):
        self.push(index, left, right)
        if left > q_right or right < q_left:
            return 0
        if q_left <= left and right <= q_right:
            return self.tree[index]
        mid = (left + right) // 2
        return (self.query(2*index+1, left, mid, q_left, q_right) +
                 self.query(2*index+2, mid+1, right, q_left, q_right))
        
