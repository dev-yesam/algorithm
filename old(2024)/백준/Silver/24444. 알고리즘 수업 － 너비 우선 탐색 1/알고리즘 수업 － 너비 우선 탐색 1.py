from collections import deque


#입력
node_num, edge_num, start = map(int, input().split())
# 그래프 입력
adjl = [[] for _ in range(node_num+1)]
for _ in range(edge_num):
    a, b = map(int, input().split())
    adjl[a].append(b)
    adjl[b].append(a)

for i in adjl:
    i.sort()

# 노드의 방문 순서
visited = [0] * (node_num+1)

# bfs 정의
def bfs(start):
    cnt = 1
    # 시작 정점에서 할일
    q = deque()
    visited[start] = cnt
    q.append(start)

    # 방문 예약과 방문
    while q:
        now = q.popleft()

        for next in adjl[now]:
            if not visited[next]:
                cnt += 1
                visited[next] = cnt
                q.append(next)

# 함수 호출
bfs(start)

# 출력
for i in visited[1:]:
    print(i)