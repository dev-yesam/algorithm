import sys

input = sys.stdin.readline

computer_num = int(input())
edges_num = int(input())

adjl = list([] for _ in range(computer_num + 1))
for _ in range(edges_num):
    a, b = map(int, input().rstrip().split())
    adjl[a].append(b)
    adjl[b].append(a)

visited = [0] * (computer_num + 1)
cnt = 0


def dfs(graph, vtx, visited):
    # cnt
    global cnt
    # 현재 위치 방문
    visited[vtx] = 1
    cnt += 1
    # 다음 위치 방문
    for new in graph[vtx]:
        if visited[new] == 0:
            dfs(graph, new, visited)


dfs(adjl, 1, visited)
print(cnt-1)
