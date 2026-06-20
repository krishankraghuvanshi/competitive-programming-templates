class UnionFind:
	def __init__(self, n):
		self.parent = list(range(n))

	def find(self, a):
		acopy = a
		while a != self.parent[a]:
			a = self.parent[a]
		while acopy != a:
			self.parent[acopy], acopy = a, self.parent[acopy]
		return a

	def union(self, a, b):
		self.parent[self.find(b)] = self.find(a)


class DisjointSetUnion:
	def __init__(self, n):
		self.parent = list(range(n))
		# self.s = set(self.parent)
		self.size = [1] * n

	def find(self, a):
		acopy = a
		while a != self.parent[a]:
			a = self.parent[a]
		while acopy != a:
			self.parent[acopy], acopy = a, self.parent[acopy]
		return a

	def union(self, a, b):
		a, b = self.find(a), self.find(b)
		if a != b:
			if self.size[a] < self.size[b]:
				a, b = b, a
			# self.s.remove(b)
			self.parent[b] = a
			self.size[a] += self.size[b]

	def set_size(self, a):
		return self.size[self.find(a)]

	def __len__(self):
		return len(self.s)

	def notfind(self, a):
		k = self.find(a)
		for j in self.s:
			if j!=k:
				return j
		return -1
'''-------------------------------------------------------------------------'''

import sys, collections, heapq

sys.setrecursionlimit(10**7)

class UnionFind:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.size = [1 for i in range(N)]
        self.components = N-1
        self.mx = 1
    def find(self, u):
        if self.parent[u]!=u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]     
    def union(self, u, v):
        root_u, root_v = self.find(u), self.find(v)
        if self.size[root_u] < self.size[root_v]:
            root_u, root_v = root_v, root_u
        if root_u != root_v:
            self.parent[root_v] = root_u
            self.size[root_u] += self.size[root_v]
            self.mx = max(self.mx, self.size[root_u])
            self.components -= 1
    def get_components(self):
        return self.components
    def get_max_component_size(self):
        return self.mx
