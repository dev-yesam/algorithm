n = int(input())

# 세로행 방문 여부
vertical = [0] * (n)

# 좌상 대각선 ( 행-열 : -(n-1)~ n-1)
# => n-1을 강제로 더해버리면 됨  0~ 2n-2
left_diagonal = [0] * (2 * n - 1)

# 우상 대각선 (행 + 열 : 0~ 2n-2)
right_diagonal = [0] * (2 * n - 1)

count = 0


def backtrack(level):
    global count

    if level == n:
        count += 1
        return

    # 재귀 호출
    for idx in range(n):
        if vertical[idx] or left_diagonal[level - idx + (n - 1)] or right_diagonal[level + idx]:
            continue
        # 다음 방문
        vertical[idx] = 1
        left_diagonal[level - idx + (n - 1)] = 1
        right_diagonal[level + idx] = 1

        backtrack(level + 1)

        # 복구
        vertical[idx] = 0
        left_diagonal[level - idx + (n - 1)] = 0
        right_diagonal[level + idx] = 0


backtrack(0)
print(count)
