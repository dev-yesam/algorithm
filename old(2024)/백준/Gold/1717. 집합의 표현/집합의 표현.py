import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def union(x, y):
    x = find_set(x)
    y = find_set(y)

    # 집합 같다면 할 게 없음
    if x == y:
        return

    # 집합 다르면
    if x < y:
        p[y] = x
    else:
        p[x] = y


def find_set(x):
    if x == p[x]:
        return x
    else:
        p[x] = find_set(p[x])
        return p[x]


n, m = map(int, input().split())
p = [i for i in range(n + 1)]
for _ in range(m):
    oper, x, y = map(int, input().split())

    if oper == 0:
        union(x,y)


    elif oper == 1:
        if find_set(x) == find_set(y):
            print("YES")
        else:
            print("NO")
