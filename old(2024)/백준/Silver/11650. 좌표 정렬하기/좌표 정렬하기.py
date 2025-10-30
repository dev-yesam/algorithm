# 11650
import sys

input = sys.stdin.readline

# 입력
n = int(input())
lst = []
for _ in range(n):
    a, b = map(int, input().split())
    lst.append((a,b))

# 정렬
lst.sort(key=lambda x: (x[0], x[1]))

# 출력
for i in lst:
    print(*i)
