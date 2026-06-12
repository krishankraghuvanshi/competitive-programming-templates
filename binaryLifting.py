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


      
      # Krishank Raghuvanshi
