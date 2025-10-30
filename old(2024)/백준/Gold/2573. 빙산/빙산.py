#######gpt 테스트 용 제출 코드 ########

from collections import deque
import sys

# 입력을 더 빠르게 받기 위해 stdin.readline 사용
input = sys.stdin.readline

# 빙산의 각 부분을 탐색하는 bfs 함수
def bfs1(r, c):
    visited[r][c] = 1  # 현재 위치를 방문 처리
    q = deque()  # BFS를 위한 큐
    q.append((r, c))  # 현재 위치를 큐에 추가

    while q:  # 큐가 비어있지 않는 동안
        cr, cc = q.popleft()  # 현재 위치

        # 상하좌우 네 방향 탐색
        for dr, dc in ((1, 0), (-1, 0), (0, -1), (0, 1)):
            nr, nc = cr + dr, cc + dc
            # 탐색 위치가 범위 내에 있고, 빙산이며, 아직 방문하지 않았다면
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] > 0 and visited[nr][nc] == 0:
                visited[nr][nc] = 1  # 방문 처리
                q.append((nr, nc))  # 큐에 추가

# 빙산이 몇 덩어리인지 세고, 녹이는 작업을 수행하는 함수
def solve():
    cnt = 0  # 빙산 덩어리 수
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0 and visited[i][j] == 0:  # 빙산이면서 아직 방문하지 않았다면
                cnt += 1  # 덩어리 수 증가
                bfs1(i, j)  # 해당 빙산 덩어리 탐색
    if cnt >= 2:
        return True  # 빙산이 2덩어리 이상으로 분리된 경우
    return False  # 빙산이 여전히 하나로 연결된 경우

N, M = map(int, input().split())  # 행, 열 입력 받기
arr = [list(map(int, input().split())) for _ in range(N)]  # 빙산 상태 입력 받기
ans = 0  # 경과한 년수

while True:
    visited = [[0] * M for _ in range(N)]  # 방문 배열 초기화
    if solve():  # 빙산이 분리되었다면
        print(ans)  # 현재까지의 년수 출력
        break
    melt_list = []  # 녹아야 할 빙산 위치와 녹는 양 저장
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0:  # 빙산인 경우
                melt = 0  # 녹는 양
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
                        melt += 1  # 인접한 바닷물의 수만큼 녹는 양 증가
                melt_list.append((i, j, melt))  # 녹아야 할 빙산과 녹는 양 저장
    # 모든 빙산이 녹았는지 확인하기 위한 변수
    all_melted = True
    for i, j, melt in melt_list:
        arr[i][j] = max(0, arr[i][j] - melt)  # 빙산 녹이기
        if arr[i][j] > 0:  # 하나라도 빙산이 남아있다면
            all_melted = False
    if all_melted:  # 모든 빙산이 녹았다면
        print(0)  # 0 출력
        break
    ans += 1  # 빙산이 분리되지 않았다면 년수 증가
