import sys
sys.setrecursionlimit(10**4)
n = int(input())

# 부모-> 자식 가중치 담을 딕셔너리
arr = dict()

# 자녀 연결할 리스트
adjl = [[] for _ in range(n + 1)]
for i in range(n - 1):
    p, c, w = map(int, input().split())
    adjl[p].append(c)
    adjl[c].append(p)
    arr[(p, c)] = w
    arr[(c, p)] = w

# 최대값
mx = 0
mn = 1


# 리프노드 to 리프노드 길이 계산 dfs
def dfs(start, weight):
    global mx, mn

    # 최대값 갱신
    if mx < weight:
        mx = weight
        mn = start

    # 현재 위치 방문
    visited[start] = 1

    # 다음 방문
    for next in adjl[start]:
        if not visited[next]:
            dfs(next, weight + arr[(start, next)])


# 말단 노드 탐색하면서, 중복 제거하는 함수

visited = [0] * (n + 1)
dfs(1, 0)
visited = [0] * (n + 1)
dfs(mn, 0)

print(mx)
