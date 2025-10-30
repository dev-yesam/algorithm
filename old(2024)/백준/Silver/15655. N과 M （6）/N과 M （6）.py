n, m = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
res =[]


def recur(num,start):

    # 종료조건
    if num == m :
        print(*res)
        return

    # 재귀호출
    for idx in range(start, n):
        res.append(lst[idx])
        recur(num+1, idx+1)
        res.pop()

recur(0,0)