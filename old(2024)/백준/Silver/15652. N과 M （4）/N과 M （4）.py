import sys
sys.setrecursionlimit(100000)
n, m =  map(int, input().split())

res = []

def recur(num,start):
    # 종료조건
    if num == m:
        print(*res)
        return

    # 재귀호출
    for i in range(start, n+1):
        res.append(i)
        recur(num+1, i)
        res.pop()

recur(0, 1)

