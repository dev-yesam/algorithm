n, m = map(int,input().split())
lst = sorted(list(map(int, input().split())))
# 수열 중복 x
# 비내림차순

res = []

def recur(num,start):
    # 종료조건
    if num == m :
        print(*res)
        return
    # 재귀 호출
    prev = 0
    for idx in range(start, n):
        if lst[idx] != prev:
            prev = lst[idx]
            res.append(lst[idx])
            recur(num+1, idx+1)
            res.pop()
recur(0,0)