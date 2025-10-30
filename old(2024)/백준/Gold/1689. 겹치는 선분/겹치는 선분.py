import sys

input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    s, e = map(int, input().split())
    lst.append((s, 1))  # 시작점
    lst.append((e, -1))  # 끝점

lst.sort()
ans = 0
count = 0
for x, y in lst:
    count += y
    ans = max(ans, count)

print(ans)
