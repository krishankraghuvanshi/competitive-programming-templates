import math
from typing import List


class LCA:
    def __init__(self, edges: List[List[int]], root: int = 1):
        self.n = len(edges) + 1
        self.m = int(math.log2(self.n)) + 2
        self.e = [[] for _ in range(self.n + 1)]
        self.d = [0] * (self.n + 1)
        self.f = [[0] * self.m for _ in range(self.n + 1)]

        for u, v in edges:
            self.e[u].append(v)
            self.e[v].append(u)

        self.dfs(root, 0)

        for i in range(1, self.m):
            for x in range(1, self.n + 1):
                self.f[x][i] = self.f[self.f[x][i - 1]][i - 1]

    def dfs(self, x: int, fa: int):
        self.f[x][0] = fa
        for y in self.e[x]:
            if y == fa:
                continue
            self.d[y] = self.d[x] + 1
            self.dfs(y, x)

    def lca(self, x: int, y: int) -> int:
        if self.d[x] > self.d[y]:
            x, y = y, x

        # raise y to the same depth as x
        diff = self.d[y] - self.d[x]
        for i in range(self.m - 1, -1, -1):
            if diff & (1 << i):
                y = self.f[y][i]

        if x == y:
            return x

        for i in range(self.m - 1, -1, -1):
            if self.f[x][i] != self.f[y][i]:
                x = self.f[x][i]
                y = self.f[y][i]

        return self.f[x][0]

    def dis(self, x: int, y: int) -> int:
        return self.d[x] + self.d[y] - self.d[self.lca(x, y)] * 2



'''----------------------------------------------------------------'''



from math import log2, ceil
from collections import defaultdict

class LCA:
    def __init__(self, n, edges, root=1):
        self.n = n
        self.L = ceil(log2(n))
        self.timer = 0

        self.g = defaultdict(list)

        for u, v in edges:
            self.g[u].append(v)
            self.g[v].append(u)

        self.tin = [0] * (n + 1)
        self.tout = [0] * (n + 1)
        self.depth = [0] * (n + 1)

        self.up = [[0] * (self.L + 1) for _ in range(n + 1)]

        self.dfs(root, root)

    def dfs(self, node, parent):

        self.timer += 1
        self.tin[node] = self.timer

        self.up[node][0] = parent

        for i in range(1, self.L + 1):
            self.up[node][i] = self.up[self.up[node][i - 1]][i - 1]

        for nei in self.g[node]:
            if nei == parent:
                continue

            self.depth[nei] = self.depth[node] + 1
            self.dfs(nei, node)

        self.timer += 1
        self.tout[node] = self.timer

    def isAncestor(self, u, v):
        return (
            self.tin[u] <= self.tin[v]
            and self.tout[u] >= self.tout[v]
        )

    def lca(self, u, v):

        if self.isAncestor(u, v):
            return u

        if self.isAncestor(v, u):
            return v

        for i in range(self.L, -1, -1):
            if not self.isAncestor(self.up[u][i], v):
                u = self.up[u][i]

        return self.up[u][0]

'''my way'''
g = defaultdict(list)

for u, v, w in edges:
    g[u].append((v, w))
    g[v].append((u, w))

LOG = 30

parent = [[-1] * (LOG) for _ in range(N)]
level = [0]*N

f = defaultdict(lambda:Counter())


def dfs(u, p):
    parent[u][0] = p

    for i in range(1, LOG):
        if parent[u][i-1] != -1:
            parent[u][i] = parent[parent[u][i-1]][i-1]

    for v, w in g[u]:
        if v == p:
            continue
        level[v] = level[u]+1

        for j, k in f[u].items():
            f[v][j] = k
        f[v][w] += 1

        dfs(v, u)

def lca(u, v):
    if level[u] < level[v]:
        u, v = v, u    
    for i in range(LOG-1, -1, -1):
        if level[u] - (1<<i) >= level[v]:
            u = parent[u][i]
    if u == v:
        return u        
    for i in range(LOG-1, -1, -1):
        if parent[u][i] != parent[v][i]:
            u = parent[u][i]
            v = parent[v][i]
    return parent[u][0]        

dfs(0, -1)
