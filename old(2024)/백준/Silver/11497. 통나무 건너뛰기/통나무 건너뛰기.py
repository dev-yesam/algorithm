# 11497

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().rstrip().split()))

    # 내림차순 정렬
    lst.sort(reverse=True)
    #10 02 13 24 35....n-1.n-3, n,n-2, n.n-1
    # 돌면서 넣기
    res = 0
    if abs(lst[1]-lst[0])>abs(lst[n-1]-lst[n-2]):
        res = abs(lst[1]-lst[0])
    else:
        res = abs(lst[n-1]-lst[n-2])
    for i in range(2,n):
        dif= abs(lst[i]-lst[i-2])
        if dif > res:
            res = dif
    
    print(res)
