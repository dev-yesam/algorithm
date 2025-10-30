# 크루스칼 알고리즘
# disjoint-set
def find_set(x):
    if x == p[x]:
        return x
    else:
        p[x] = find_set(p[x])
        return p[x]

def union_set(x,y):
    x = find_set(x)
    y = find_set(y)

    if x==y:
        return # 아무것도 안함. 근데 이미 다른 것만 함.

    # 연결해야 한다면
    if x < y:
        p[y] = x
    else:
        p[x] = y


# 크루스칼 사용

v, e = map(int, input().split())
edges = []
for _ in range(e):
    start, end, weight = map(int, input().split())
    edges.append((start, end, weight))

sum_weight = 0

# edges 오름차순 정렬
edges.sort(key=lambda x: x[2])

# disjoint set 준비
p = [i for i in range(v + 1)]

# 간선들 확인
for start, end, weight in edges:

    # start와 end 가 연결되어있다? => 뭐 안하면 됨
    if find_set(start) == find_set(end):
        continue

    # 연결 안되어 있다? => 최소 신장 트리 확장
    union_set(start, end)
    sum_weight += weight

print(sum_weight)