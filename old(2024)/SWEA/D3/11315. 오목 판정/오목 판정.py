def f(i, j):
    # 우, 하, 좌하, 우하
    for dr, dc in [(0, 1), (1, 0), (1, -1), (1, 1)]:
        cnt = 1
        for power in range(1, 5):
            nr, nc = i + dr * power, j + dc * power
            if not (0 <= nr < n and 0 <= nc < n) :
                break
            if arr[nr][nc] !=  'o':
                break
        else:
            return True
    return False

def solve():
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'o':
                if f(i, j):
                    return 'YES'
    return 'NO'


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [input() for _ in range(n)]

    ans = solve()
    print(f'#{tc}', ans)
