from heapq import heappush, heappop


def dijkstra(start):
    dists = [INF] * (v+1)
    dists[start] = 0

    pq = []
    heappush(pq, (0,start))

    while pq:
        # 꺼내기
        now_dist, now_node = heappop(pq)

        if now_dist > dists[now_node]:
            continue


        # 다음 반복
        for next_weight, next_node in adjl[now_node]:
            new_dist = now_dist + next_weight
            if new_dist < dists[next_node]:
                heappush(pq, (new_dist, next_node))
                dists[next_node] = new_dist

    return dists


v, e = map(int, input().split())
start = int(input())
adjl = [[] for _ in range(v + 1)]
for _ in range(e):
    s, e, w = map(int, input().split())
    adjl[s].append((w, e))


INF = 200000
ans = dijkstra(start)
for i in ans[1:]:
    if i == INF:
        print("INF")
    else:
        print(i)
