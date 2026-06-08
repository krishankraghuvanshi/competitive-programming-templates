# -------------------------------------------------
# Advanced Tree Template
# -------------------------------------------------
#
# Includes:
# 1. DFS Order / Euler Tour
# 2. Parent
# 3. Depth
# 4. Subtree Size
# 5. Binary Lifting
# 6. LCA (Lowest Common Ancestor)
# 7. kth Parent Query
# 8. Distance Between Nodes
#
# Preprocessing -> O(n log n)
# LCA Query     -> O(log n)
# kth Parent    -> O(log n)
# -------------------------------------------------


from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)


class Tree:

    def __init__(self, n):

        self.n = n

        self.g = defaultdict(list)

        # maximum power for binary lifting
        self.LOG = n.bit_length()

        # up[j][i] = 2^j-th parent of node i
        self.up = [[-1] * n for _ in range(self.LOG)]

        self.depth = [0] * n

        self.parent = [-1] * n

        self.subtree = [1] * n

        # euler timings
        self.tin = [0] * n
        self.tout = [0] * n
        self.timer = 0

    # add edge
    def add_edge(self, u, v):

        self.g[u].append(v)
        self.g[v].append(u)

    # -----------------------------------------
    # DFS + Binary Lifting Build
    # -----------------------------------------
    def dfs(self, node, par):

        self.parent[node] = par

        self.tin[node] = self.timer
        self.timer += 1

        # first parent
        self.up[0][node] = par

        # build binary lifting table
        for j in range(1, self.LOG):

            prev = self.up[j - 1][node]

            if prev != -1:
                self.up[j][node] = self.up[j - 1][prev]

        for nei in self.g[node]:

            if nei == par:
                continue

            self.depth[nei] = self.depth[node] + 1

            self.dfs(nei, node)

            self.subtree[node] += self.subtree[nei]

        self.tout[node] = self.timer
        self.timer += 1

    # preprocess tree
    def build(self, root=0):

        self.dfs(root, -1)

    # -----------------------------------------
    # kth parent of node
    # -----------------------------------------
    def kth_parent(self, node, k):

        for j in range(self.LOG):

            if node == -1:
                break

            # if j-th bit is set
            if (k >> j) & 1:
                node = self.up[j][node]

        return node

    # -----------------------------------------
    # check if u is ancestor of v
    # -----------------------------------------
    def is_ancestor(self, u, v):

        return (
            self.tin[u] <= self.tin[v]
            and self.tout[u] >= self.tout[v]
        )

    # -----------------------------------------
    # Lowest Common Ancestor
    # -----------------------------------------
    def lca(self, u, v):

        if self.is_ancestor(u, v):
            return u

        if self.is_ancestor(v, u):
            return v

        # lift u upwards
        for j in range(self.LOG - 1, -1, -1):

            if self.up[j][u] != -1 and not self.is_ancestor(self.up[j][u], v):

                u = self.up[j][u]

        return self.up[0][u]

    # -----------------------------------------
    # distance between nodes
    # -----------------------------------------
    def distance(self, u, v):

        l = self.lca(u, v)

        return (
            self.depth[u]
            + self.depth[v]
            - 2 * self.depth[l]
        )


# ---------------- Example ----------------

n = 7

tree = Tree(n)

edges = [
    [0, 1],
    [0, 2],
    [1, 3],
    [1, 4],
    [2, 5],
    [2, 6]
]

for u, v in edges:
    tree.add_edge(u, v)

tree.build(0)

print("Depth:", tree.depth)

print("Subtree:", tree.subtree)

print("LCA of 3 and 4:", tree.lca(3, 4))

print("LCA of 3 and 6:", tree.lca(3, 6))

print("Distance between 3 and 6:", tree.distance(3, 6))

print("2nd parent of 4:", tree.kth_parent(4, 2))
