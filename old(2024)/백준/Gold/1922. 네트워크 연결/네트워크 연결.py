from heapq import heappush, heappop
import sys

input = sys.stdin.readline


def prim(start):
    visited = [0] * (n + 1)
    total = 0
    heap = []
    heappush(heap, (0, start))
    cnt = 0


    while heap:
        # 꺼내기
        weight, now = heappop(heap)

        # 방문한 적 있는 애면
        if visited[now]:
            continue

        visited[now] = 1
        total += weight
        cnt += 1
        if cnt == n:
            break

        # 다음 방문
        for next_weight, next_node in adjl[now]:
            if not visited[next_node]:
                heappush(heap,(next_weight, next_node))

    return total


n = int(input())
m = int(input())
adjl = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, w = map(int, input().split())
    adjl[s].append((w, e))
    adjl[e].append((w, s))

# 프림 알고리즘
ans = prim(1)
print(ans)
