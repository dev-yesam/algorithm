import sys
sys.setrecursionlimit(10**5)
n, m, r = map(int, input().split())
adjl = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    adjl[a].append(b)
    adjl[b].append(a)

for node in adjl:
    node.sort(reverse=True)


def dfs(now, order):
    visited[now] = order

    for next in adjl[now]:
        if visited[next] == -1:
            dfs(next, order + 1)


dfs(r, 0)

for i in range(1, n + 1):
    print(visited[i])
