
def solve(arr, cmp):
    # 가로 줄 확인
    for i in range(9):
        temp = 0
        for j in range(9):
            temp = temp | (1<<arr[i][j])
        if temp != cmp:
            return 0

    # 세로 줄 확인
    for j in range(9):
        temp = 0
        for i in range(9):
            temp = temp | (1<<arr[i][j])
        if temp != cmp:

            return 0

    # 9칸 확인
    for k in range(3):
        for l in range(3):
            temp = 0
            for i in range(3):
                for j in range(3):
                    temp = temp | (1<<arr[i+3*k][j+3*l])
            if temp != cmp:
                return 0

    # 모두 통과했다면
    return 1

t = int(input())
for tc in range(1, t + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    cmp = (1 << 10) - 2 # 2의 1~9 번째가 자리 1로 표기됨. 2^0의 자리는 0으로 표기

    ans = solve(arr, cmp)
    print(f'#{tc} {ans}')
