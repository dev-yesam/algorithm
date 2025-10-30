n, m = map(int, input().split())

adjl = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    adjl[a].append(b)
    adjl[b].append(a)

# dfs 수행하면서 연결된 버틱스들 확인
# 이전에 방문되지 않은 거면 다시 dfs 수행

visited = [0] * (n+1)

def dfs(adjl, vtx):
    visited[vtx] = 1

    for i in adjl[vtx]:
        if not visited[i] :
            dfs(adjl,i)

cnt = 0
for i in range(1,n+1):
    if visited[i]==0:
       cnt+=1
       dfs(adjl, i)

print(cnt)