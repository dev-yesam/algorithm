# 입력 받기
import sys

n, k = map(int, sys.stdin.readline().split())
cats = list(map(int,sys.stdin.readline().split()))
cats.sort(reverse=True)
cnt= 0

# 인덱스 두 개
p1, p2 = 0, n-1

while p1<p2:
    if cats[p1] + cats[p2] <= k:
        p1 +=1
        p2 -=1
        cnt +=1
    else:
        p1 +=1

print(cnt)
