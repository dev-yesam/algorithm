from heapq import heappush, heappop


def dijkstra(start):
    # 출발점
    pq = []
    dists = [INF] * (n + 1)
    dists[start] = 0
    heappush(pq, (0, start))  # 누적거리, 이전 노드

    # while
    while pq:
        now_dist, now_node = heappop(pq)

        if now_dist > dists[now_node]:
            continue

        for next_weight, next_node in adjl[now_node]:
            next_dist = now_dist + next_weight

            if next_dist < dists[next_node]:
                dists[next_node] = next_dist
                heappush(pq, (next_dist, next_node))

                # 직전 점이 시작점이라면?
                if now_node == start:
                    stopovers[start][next_node] = next_node
                else:
                    stopovers[start][next_node] = stopovers[start][now_node]


# n, m  = 집하장 개수, 경로의 수
n, m = map(int, input().split())
adjl = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, w = map(int, input().split())
    adjl[s].append((w, e))
    adjl[e].append((w, s))

INF = 210000
stopovers = [["-"] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dijkstra(i)

for i in range(1, n + 1):
    print(*stopovers[i][1:])
