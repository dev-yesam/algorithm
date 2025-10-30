from collections import deque

N, target = map(int, input().split())

# N < target
# [1] while 2*N < target:
# [2] N +1...
if N >= target:
    cnt = N - target
    print(cnt)

# N > target
# N -1....
else:
    def bfs():
        # 시작점
        # [1] 사전 방문 처리
        visited = [0] * (200001)
        visited[N] = 1

        # [2] 방문 행동 -> 없음
        # [3] 방문 예약
        q = deque()
        q.append(N)

        # 방문 예약 처리
        while q:
            now = q.popleft()
            if now == target:
                return visited[now] - 1

            for next in (now - 1, now + 1, now * 2):
                if 0 <= next <= 200000 and visited[next] == 0:
                    visited[next] = visited[now] + 1
                    q.append(next)

        # 만약 뭐가 잘못됐다면
        return -1
    
    cnt = bfs()
    print(cnt)
