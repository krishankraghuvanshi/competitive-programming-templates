import sys, math, collections, bisect, heapq, functools, itertools

input = lambda:sys.stdin.readline().strip()

sys.setrecursionlimit(10000000)

def solve():
    N, Q = map(int, input().split())
    nums = list(map(int, input().split()))
    nums = [0] + nums

    LOG = 20

    parent = [[0] * LOG for _ in range(N+1)]

    for i in range(1, N+1):
        parent[i][0] = nums[i]

    for i in range(1, N+1):
        for j in range(1, LOG):
            parent[i][j] = parent[parent[i][j-1]][j-1]

    def lift(x, k):
        for i in range(LOG):
            if k & (1<<i):
                x = parent[x][i]
        return x
    
    visited = [0] * (N+1)
    in_cycle = [False] * (N+1)
    cycle_pos = [0] * (N+1)
    cycle_id = {}
    depth = [0] * (N+1)
    cycle_length = [0] * (N+1)
    id = 1

    for i in range(1, N+1):

        if visited[i] == 0:
            j = i
            path = []
            while visited[j] == 0:
                visited[j] = 1
                path.append(j)
                j = nums[j]
            if visited[j] == 1:
                cycle_nodes = []
                while len(path) and path[-1] != j:
                    cycle_nodes.append(path.pop())
                cycle_nodes.append(path.pop()) 
                cycle_nodes.reverse()

                c_len = len(cycle_nodes)
                cycle_length[id] = c_len

                for pos, node in enumerate(cycle_nodes):
                    cycle_pos[node] = pos
                    in_cycle[node] = True
                    cycle_id[node] = id
                    depth[node] = 0
                    visited[node] = 2
                id += 1

            for node in path:
                visited[node] = 2

    rev_adj = collections.defaultdict(list)

    for i in range(1, N+1):
        rev_adj[nums[i]].append(i)

    def dfs(node):

        for nei in rev_adj[node]:
            if in_cycle[nei]:
                continue
            depth[nei] = depth[node]+1
            cycle_id[nei] = cycle_id[node]
            dfs(nei)

    for i in range(1, N+1):
        if in_cycle[i]:
            dfs(i)
 
solve()
