from heapq import heappush, heappop


def prim(start):
    pq = []
    mst = [0] * n
    e_price = 0
    heappush(pq, (0, start))
    cnt = 0

    while pq:
        weight, now = heappop(pq)

        # 방문했던 곳인지
        if mst[now]:
            continue

        # 방문처리
        mst[now] = 1
        e_price += weight

        # 최적화
        cnt += 1
        if cnt == n:
            break

        # 다음 방문
        for next in range(n):
            if mst[next]:
                continue
            new_weight = e * ((x_lst[next] - x_lst[now]) ** 2 + (y_lst[next] - y_lst[now]) ** 2)
            heappush(pq, (new_weight, next))

    return e_price


t = int(input())
for tc in range(1, t + 1):
    n = int(input())  # 섬 개수
    x_lst = list(map(int, input().split()))  # 섬 좌표
    y_lst = list(map(int, input().split()))  # 섬 좌표
    e = float(input())  # 세율

    ans = prim(0)
    print(f'#{tc}', round(ans))
