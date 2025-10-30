n, m = map(int, input().split())
lst = []


def bt(start, end):
    if start > end:
        print(*lst)
        return

    for i in range(1,n+1):
        if i not in lst:
            lst.append(i)
            bt(start + 1,end)
            lst.pop()

bt(1,m)