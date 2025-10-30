n, m = map(int, input().split())

res =[]

def recur(num):

    # 종료조건
    if num == m:
        print(*res)
        return

    # 재귀호출
    for i in range(1,n+1):
        res.append(i)
        recur(num+1)
        #복구
        res.pop()


recur(0)
