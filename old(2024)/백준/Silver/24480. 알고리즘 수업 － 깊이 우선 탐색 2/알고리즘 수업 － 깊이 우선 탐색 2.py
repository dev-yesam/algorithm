import sys
sys.setrecursionlimit(10**5)

vtx_n , edge_num, start = map(int, input().split())
adjl = list([] for _ in range(vtx_n+1))
for _ in range(edge_num):
    a, b = map(int,input().split())
    adjl[a].append(b)
    adjl[b].append(a)
# 정점 내림차순 방문
for v in adjl:
    v.sort(reverse=True)

# 방문 여부
visited = [0] * (vtx_n+1)
num = 1
def dfs(start):
    global num


    # 방문 업무
    visited[start] = num
    num += 1

    # 재귀 호출
    for vtx in adjl[start]:
        if not visited[vtx]:
            dfs(vtx)

dfs(start)
for i in visited[1:]:
    print(i)