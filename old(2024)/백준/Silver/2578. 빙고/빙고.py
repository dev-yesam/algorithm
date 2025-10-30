# 2578 빙고

# 빙고 배열 입력
arr = [list(map(int, input().split())) for _ in range(5)]

# 사회자 번호 리스트
lst = []
for _ in range(5):
    lst.extend(map(int, input().split()))

# 번호 지운 횟수
cnt = 0

# 번호 리스트 순회
for num in lst:

    # 빙고 횟수
    bingo = 0

    for r in range(5):
        if num in arr[r]:
            idx = arr[r].index(num)
            arr[r][idx] = 0
            break

    cnt += 1
    # 빙고 확인

    # 가로
    for r in range(5):
        if all(i == 0 for i in arr[r]):
            bingo += 1

    # 세로
    for c in range(5):
        if all(arr[i][c] == 0 for i in range(5)):
            bingo += 1

    # 우상 대각선
    if all(arr[r][r] == 0 for r in range(5)):
        bingo += 1

    # 좌상 대각선
    if all(arr[r][4 - r] == 0 for r in range(5)):
        bingo += 1

    # 세 번 빙고가 됐다면 종료
    if bingo >= 3:
        print(cnt)
        break
