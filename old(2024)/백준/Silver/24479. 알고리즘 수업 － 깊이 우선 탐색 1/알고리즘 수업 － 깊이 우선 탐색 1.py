import sys
sys.setrecursionlimit(10**5)

vtx_num, edges_num, start = map(int, sys.stdin.readline().rstrip().split())

adjl = [[] for _ in range(vtx_num + 1)]
for _ in range(edges_num):
    a, b = map(int, sys.stdin.readline().split())
    adjl[a].append(b)
    adjl[b].append(a)

for vtx in adjl:
    vtx.sort()

cnt = 1
visited = [0] * (vtx_num + 1)


def dfs(graph, start, visited):
    global cnt
    # 현재 위치 방문
    now = start
    visited[now] = cnt
    cnt += 1
    for vtx in graph[now]:
        if visited[vtx] == 0:
            dfs(graph, vtx, visited)

dfs(adjl, start, visited)

for vtx in visited[1:]:
    print(vtx)
