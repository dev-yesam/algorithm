# dfs로 풀어봄. bfs로도 가능할 듯.

# 걍 1병당 50미터 간다고 보면 됨.
# 1 박스에 20 병
# 박스에 최대 20 병 담고 갈 수 있음
# 결국 1번 편의점 들릴 때마다 1000m 씩 갈 수 있음.

def dfs(x, y):
    global ans
    # 마지막 위치에 도달한다면?
    if x==lst[-1][0] and y==lst[-1][1]:
        ans = 'happy'

    # 재귀호출
    for next in range(n+2):
        # 방문하지 않았고, 거리가 1000 이하여야함.
        if not visited[next] and abs(lst[next][0]-x) + abs(lst[next][1]-y) <= 1000 :
            visited[next] = 1
            dfs(lst[next][0], lst[next][1])




t = int(input())
for tc in range(1, t + 1):
    # 편의점 개수
    n = int(input())

    # 위치 정보 입력
    lst = []
    for _ in range(n + 2):
        x, y = map(int, input().split())
        lst.append((x, y))

    # dfs
    visited = [0] * (n+2) # 걍 모든 편의점, 집, 페스티벌
    # 0번 : 집, 1~n 편의점, n+1 번 인덱스 페스티벌
    ans = 'sad' # 디폴트
    dfs(lst[0][0], lst[0][1])
    
    # 출력
    print(ans)