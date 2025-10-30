import sys

input = sys.stdin.readline


def find_set(x):
    if p[x] == x:
        return x
    p[x] = find_set(p[x])
    return p[x]


def union_set(x, y):
    x = find_set(x)
    y = find_set(y)
    if y == x:
        return

    if x > y:
        p[y] = x
    else:
        p[x] = y


n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda x: x[2])
# 크루스칼로 다 연결한다음에, 맨 마지막 경로만 없애면 되겠는데?

p = [i for i in range(n + 1)]
cnt = 0
total_weight = 0

if n > 2:
    for a, b, c in edges:
        if find_set(a) == find_set(b):
            continue

        union_set(a, b)
        total_weight += c

        cnt += 1
        if cnt == n - 2:
            break

print(total_weight)
