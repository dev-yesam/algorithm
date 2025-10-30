from heapq import heappush, heappop


# 다익스트라
def dijkstra(start, goal):
    # 시작점
    INF = 10 ** 8
    dists = [INF] * (n + 1)
    dists[start] = 0
    pq = []
    heappush(pq, (0, start))

    # 방문 예약
    while pq:
        # 꺼내기
        now_weight, now = heappop(pq)

        # 효율화
        if dists[now] < now_weight:
            continue


        # 다음 방문
        for next_weight, next in adjl[now]:
            dist = next_weight + dists[now]

            if dists[next] > dist:
                heappush(pq, (dist, next))
                dists[next] = dist


    return dists[goal]


# 도시 개수 n
n = int(input())
# 버스(간선) 개수 m
m = int(input())
adjl = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, w = map(int, input().split())
    adjl[s].append((w, e))

# 출발지와 도착지
start, goal = map(int, input().split())

# 다익스트라
ans = dijkstra(start, goal)

print(ans)
