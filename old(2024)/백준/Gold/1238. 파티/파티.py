from heapq import heappush, heappop


def dijkstra(start):
    pq = []
    heappush(pq, (0, start))
    dists[start][start] = 0

    while pq:

        # 꺼내기
        distance, now_node = heappop(pq)

        if distance > dists[start][now_node]:
            continue

        for next_weight, next_node in adjl[now_node]:
            new_distance = distance + next_weight

            if new_distance >= dists[start][next_node]:
                continue

            dists[start][next_node] = new_distance
            heappush(pq, (new_distance, next_node))


n, m, x = map(int, input().split())
adjl = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, w = map(int, input().split())
    adjl[s].append([w, e])
    # adjl[e].append([w, s])

INF = int(1e8)
dists = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dijkstra(i)

ans_lst = [0]*(n+1)
for i in range(1, n+1):
    ans_lst[i] = dists[i][x] + dists[x][i]

print(max(ans_lst))