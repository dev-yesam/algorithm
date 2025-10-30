# 5212

# 다도해의 지도는 R*C 크기의 그리드로 나타낼 수 있다. 'X'는 땅을 나타내고, '.'는 바다
# 인접한 세 칸 또는 네 칸에 바다가 있는 땅은 모두 잠겨버린다
# 지도의 크기도 작아져야 한다. 지도의 크기는 모든 섬을 포함하는 가장 작은 직사각형이다
# 50년이 지난 후에도 섬은 적어도 한 개 있다.
# 지도에 없는 곳, 지도의 범위를 벗어나는 칸은 모두 바다이다.


R, C = map(int, input().split())

map = [list(input()) for _ in range(R)]

# 델타 : 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 섬 넣을 리스트
island = []


# 범위를 넘는지 확인 함수
def in_area(x, y):
    if 0 <= x < R and 0 <= y < C:
        return True
    else:
        return False


# 모든 칸 순회하며 섬 확인
for i in range(R):
    for j in range(C):

        # 섬이 주변에 2개 이상이어야 한다.
        island_num = 0
        for d in range(4):
            if map[i][j] == 'X':
                nr = i + dr[d]
                nc = j + dc[d]
                if in_area(nr, nc) and map[nr][nc] == 'X':
                    island_num += 1

        # 섬이 2개 이상이다?
        if island_num >= 2:
            island.append((i, j))

# 새로 map 리스트 만들기
# 섬 위치 최대 최소
M_r, m_r, M_c, m_c = 0, R - 1, 0, C - 1

# 최대 최소 조사
for i in island:
    if i[0] > M_r:
        M_r = i[0]
    if i[0] < m_r:
        m_r = i[0]
    if i[1] > M_c:
        M_c = i[1]
    if i[1] < m_c:
        m_c = i[1]

# map 변화 시키기
map = [['.' for _ in range(C)] for _ in range(R)]
for i in island:
    map[i[0]][i[1]] = 'X'

# map 출력
for i in range(m_r, M_r + 1):
    for j in range(m_c, M_c + 1):
        print(map[i][j], end='')
    print()
