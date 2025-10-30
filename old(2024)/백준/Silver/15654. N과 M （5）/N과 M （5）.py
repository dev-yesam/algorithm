import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
res =  []

def recur(num):
    #가지치기 x
    # 종료조건
    if num == m:
        print(*res)
        return
    # 재귀호출
    for i in lst:
        if i not in res:
            res.append(i)
            recur(num+1)
            res.pop()

recur(0)