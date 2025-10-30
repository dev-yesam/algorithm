def make_set(N):
    return [i for i in range(N + 1)]


def find_set(x):
    if parents[x] == x:
        return x  # 자기 자신이 대표

    # 경로 압축
    parents[x] = find_set(parents[x])
    return parents[x]


def union_set(x, y):
    x = find_set(x)
    y = find_set(y)

    # 같아?
    if x == y:
        return  # 암것도 안함

    if rank[x] > rank[y]:
        parents[y] = x

    elif rank[x] < rank[x]:
        parents[x] = y

    else:
        parents[y] = x
        rank[x] += 1


n = int(input())  # 도시의 수 (그래프의 노드)
m = int(input())  # 여행갈 도시의 수
adjm = [list(map(int, input().split())) for _ in range(n)]
tourist = list(map(int, input().split()))

parents = make_set(n)
rank = [i for i in range(n + 1)]

# 도로 연결하기
for i in range(n):
    for j in range(n):
        if i > j and adjm[i][j]:
            union_set(i+1, j+1)

ans = "YES"
prev = find_set(tourist[0])
for t in tourist[1:]:
    if find_set(t) != prev:
        ans = "NO"
        break

print(ans)