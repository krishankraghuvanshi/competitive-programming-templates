# -------------------------------------------------
# Advanced Graph Template
# -------------------------------------------------
#
# Includes:
# 1. BFS
# 2. DFS
# 3. Dijkstra
# 4. Topological Sort
# 5. Cycle Detection
# 6. Union Find (DSU)
#
# Supports:
# - Directed Graph
# - Undirected Graph
# - Weighted Graph
#
# -------------------------------------------------


from collections import defaultdict, deque
import heapq


class Graph:

    def __init__(self, n):

        self.n = n

        # adjacency list
        # g[u] = [(v, weight)]
        self.g = defaultdict(list)

    # -----------------------------------------
    # add edge
    # directed=False -> undirected graph
    # -----------------------------------------
    def add_edge(self, u, v, w=1, directed=False):

        self.g[u].append((v, w))

        if not directed:
            self.g[v].append((u, w))

    # -----------------------------------------
    # BFS (shortest path in unweighted graph)
    # -----------------------------------------
    def bfs(self, start):

        dist = [-1] * self.n

        q = deque([start])

        dist[start] = 0

        while q:

            node = q.popleft()

            for nei, w in self.g[node]:

                if dist[nei] != -1:
                    continue

                dist[nei] = dist[node] + 1

                q.append(nei)

        return dist

    # -----------------------------------------
    # DFS
    # -----------------------------------------
    def dfs(self, start):

        vis = [False] * self.n

        def dfs_helper(node):

            vis[node] = True

            print(node, end=" ")

            for nei, w in self.g[node]:

                if not vis[nei]:
                    dfs_helper(nei)

        dfs_helper(start)

        print()

    # -----------------------------------------
    # Dijkstra (weighted shortest path)
    # -----------------------------------------
    def dijkstra(self, start):

        dist = [float("inf")] * self.n

        dist[start] = 0

        pq = [(0, start)]

        while pq:

            d, node = heapq.heappop(pq)

            # skip outdated state
            if d > dist[node]:
                continue

            for nei, w in self.g[node]:

                nd = d + w

                if nd < dist[nei]:

                    dist[nei] = nd

                    heapq.heappush(pq, (nd, nei))

        return dist

    # -----------------------------------------
    # Topological Sort (Kahn's Algorithm)
    # Only for DAG
    # -----------------------------------------
    def topo_sort(self):

        indegree = [0] * self.n

        # calculate indegree
        for u in self.g:

            for v, w in self.g[u]:
                indegree[v] += 1

        q = deque()

        for i in range(self.n):

            if indegree[i] == 0:
                q.append(i)

        topo = []

        while q:

            node = q.popleft()

            topo.append(node)

            for nei, w in self.g[node]:

                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)

        return topo

    # -----------------------------------------
    # Cycle Detection (Undirected Graph)
    # -----------------------------------------
    def has_cycle_undirected(self):

        vis = [False] * self.n

        def dfs(node, parent):

            vis[node] = True

            for nei, w in self.g[node]:

                if not vis[nei]:

                    if dfs(nei, node):
                        return True

                elif nei != parent:
                    return True

            return False

        for i in range(self.n):

            if not vis[i]:

                if dfs(i, -1):
                    return True

        return False


# -------------------------------------------------
# Disjoint Set Union (Union Find)
# -------------------------------------------------

class DSU:

    def __init__(self, n):

        self.parent = list(range(n))

        self.size = [1] * n

    # find representative
    def find(self, x):

        if self.parent[x] != x:

            # path compression
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    # union by size
    def union(self, a, b):

        pa = self.find(a)
        pb = self.find(b)

        if pa == pb:
            return False

        # attach smaller to larger
        if self.size[pa] < self.size[pb]:
            pa, pb = pb, pa

        self.parent[pb] = pa

        self.size[pa] += self.size[pb]

        return True


# ---------------- Example ----------------

g = Graph(6)

g.add_edge(0, 1, 4)
g.add_edge(0, 2, 1)
g.add_edge(2, 1, 2)
g.add_edge(1, 3, 1)
g.add_edge(2, 3, 5)
g.add_edge(3, 4, 3)

print("BFS:", g.bfs(0))

print("DFS:")
g.dfs(0)

print("Dijkstra:", g.dijkstra(0))

print("Cycle Exists:", g.has_cycle_undirected())


# ---------------- DSU Example ----------------

dsu = DSU(5)

dsu.union(0, 1)
dsu.union(1, 2)

print(dsu.find(2) == dsu.find(0))  # True
print(dsu.find(3) == dsu.find(0))  # False
