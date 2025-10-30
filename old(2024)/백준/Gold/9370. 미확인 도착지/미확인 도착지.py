# 최단 경로가 여러 개일 수 있음
# 만약 최단 거리가,
# 시작점 -> g -> 도착점과 같거나, 시작점 -> h -> 도착점과 같다면,
# 해당 목적지 후보는 출력하면 됨.
from heapq import heappop, heappush
import sys

input = sys.stdin.readline


def dijkstra(start, dists):
    pq = []
    heappush(pq, (0, start))
    dists[start] = 0

    while pq:
        dist, now = heappop(pq)

        if dists[now] < dist:
            continue

        for next_weight, next in adjl[now]:
            next_dist = dist + next_weight
            if next_dist < dists[next]:
                dists[next] = next_dist
                heappush(pq, (next_dist, next))


t = int(input())
for _ in range(t):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    adjl = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, w = map(int, input().split())
        adjl[a].append((w, b))
        adjl[b].append((w, a))

    # 후보군 목적지
    c_lst = [int(input()) for _ in range(t)]
    c_lst.sort()

    # 거리
    INF = 2000000
    dists_s = [INF] * (n + 1)
    dists_g = [INF] * (n + 1)
    dists_h = [INF] * (n + 1)

    # 다익스트라
    dijkstra(s, dists_s)
    dijkstra(g, dists_g)
    dijkstra(h, dists_h)

    # g-h 거리
    for d in adjl[g]:
        if d[1] == h:
            gh_dist = d[0]

    # 후보군 판단
    for c in c_lst:
        # 목적지까지 거리 = 시작점->g 거리 + g->h + h->목적지 거리
        if (dists_s[c] == dists_s[g] + gh_dist + dists_h[c]) or (dists_s[c] == dists_s[h] + gh_dist + dists_g[c]):
            print(c, end=' ')
    print()
