def ver_cnt(col):
    cnt = 0
    prev = False
    for row in range(n):
        # red가 나오면?
        if arr[row][col] == 1:
            prev = True

        # blue가 나오고 이전에 red가 있었다면?
        elif arr[row][col] == 2 and prev:
            cnt += 1
            prev = False

    return cnt


t = 10
for tc in range(1, 11):

    n = int(input())  # 100
    arr = [list(map(int, input().split())) for _ in range(n)]

    total_cnt = 0
    # 1열~n열 돌아가면서
    for col in range(n):
        total_cnt += ver_cnt(col)

    ### 함수 처리
    # 각 열에서 red 있다면
    # 뒤에 blue가 나오는지
    # 그리고 또 뒤에 red가 나오면
    # 또 뒤에 blue 가 있는지.

    print(f'#{tc} {total_cnt}')
