import sys
input = sys.stdin.readline
M = int(input())
S = set()
for _ in range(M):

    lst = input().split()
    dir = lst[0]
    if len(lst)>=2:
        num = int(lst[1])
    if dir == 'add' :
        S.add(num)
    elif dir == 'remove':
        S.discard(num)

    elif dir == 'check':
        if num in S:
            print(1)
        else:
            print(0)
    elif dir == 'toggle':
        if num in S:
            S.discard(num)
        else:
            S.add(num)
    elif dir == 'all':
        S = set(range(1,21))
    else :
        S.clear()


