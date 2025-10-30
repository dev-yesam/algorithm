from heapq import heappush, heappop


def dijkstra(sr, sc):
    distance = [[10 ** 7] * n for _ in range(n)]

    heap = []
    heappush(heap, (arr[sr][sc], sr, sc))
    distance[sr][sc] = arr[sr][sc]

    while heap:
        dist, cr, cc = heappop(heap)

        # 효율화
        if dist > distance[cr][cc]:
            continue

        for nr, nc in [(cr + 1, cc), (cr, cc + 1), (cr - 1, cc), (cr, cc - 1)]:
            if 0 <= nr < n and 0 <= nc < n:
                new_dist = dist + arr[nr][nc]

                if new_dist < distance[nr][nc]:
                    distance[nr][nc] = new_dist
                    heappush(heap, (new_dist, nr, nc))

    return distance[n - 1][n - 1]

tc = 0
while True:
    # 가로 세로 칸 수
    n = int(input())
    if n == 0 : break

    tc += 1
    # 지역 맵
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 출력
    ans = dijkstra(0, 0)
    print(f'Problem {tc}: {ans}')
