import heapq
import sys
input = sys.stdin.readline

heap = []

n = int(input())
for _ in range(n):

    x = int(input())

    # 0이다?
    if x == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
        continue

    # 0이 아니다?
    heapq.heappush(heap, x)