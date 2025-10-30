n, m = map(int,input().split())
lst = [i for i in range(1,n+1)]
res = []

# 백트래킹
# 0, 1, .... m 스탑.
def recur(num):

    if num == m:
        print(*res)
        return

    for i in lst:
        if i not in res:
            res.append(i)
            recur(num+1)

            res.pop()

recur(0)