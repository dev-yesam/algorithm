from heapq import heappush, heappop
import math


def prim(start):
    visited = [0] * n
    pq = []
    total = 0
    cnt = 0

    # 시작점
    heappush(pq, (0, start))

    # 방문 예약
    while pq:
        # 꺼내기
        weight, now = heappop(pq)

        # 이전에 꺼낸 거였다면?
        if visited[now]:
            continue

        # 아니라면?
        visited[now] = 1
        total += weight
        cnt += 1
        if cnt == n:
            break

        # 다음 방문 예약
        for next in range(n):
            if not visited[next]:
                next_weight = math.sqrt((lst[now][0] - lst[next][0]) ** 2 + (lst[now][1] - lst[next][1]) ** 2)
                heappush(pq, (next_weight, next))

    return total


# 간선 최대까지 있을 수 있음
# 프림 알고리즘

n = int(input())
lst = [list(map(float, input().split())) for _ in range(n)]

# 0~ n-1번까지
ans = prim(0)

print(ans)