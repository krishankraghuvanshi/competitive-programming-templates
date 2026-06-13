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
'''----------------------------------------------------------------'''
               #imo this is more cool way of writing it
import sys, collections, math

input = lambda:sys.stdin.readline().strip()

sys.setrecursionlimit(10**7)

def solve():
    N, M = map(int, input().split())

    G = collections.defaultdict(lambda:[])
    for _ in range(N-1):
        u, v = map(int, input().split())
        u, v = u-1, v-1
        G[u].append(v)
        G[v].append(u)

    L = math.ceil(math.log2(N)) 

    parent = [[-1] * (L+1) for _ in range(N)]
    level = [0] * N

    def dfs(u, p):
        parent[u][0] = p
        for i in range(1, L+1):
            if parent[u][i-1] != -1:
                parent[u][i] = parent[parent[u][i-1]][i-1]

        for v in G[u]:
            if v == p:
                continue
            level[v] = level[u]+1
            dfs(v, u)
    
    def lca(u, v):
        if level[u] < level[v]:
            u, v = v, u
        for i in range(L, -1, -1):
            if level[u] - (1<<i) >= level[v]:
                u = parent[u][i]    
        if u == v:
            return u
        for i in range(L, -1, -1):
            if parent[u][i] != -1 and parent[u][i] != parent[v][i]:
                u = parent[u][i]
                v = parent[v][i]
        return parent[u][0]
    
    count = [0] * N 
    def dfs1(u, p):
        for v in G[u]:
            if v == p:
                continue
            dfs1(v, u)
            count[u] += count[v]
    
    dfs(0, -1)



      
      # Krishank Raghuvanshi
