def count(lst):
    M = cnt = 1
    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            cnt += 1
            M = max(M, cnt)
        else:
            cnt = 1
    return M


def solve(arr, arr_t):
    mx = 0
    for i in range(n):
        for j in range(n - 1):
            # 우측 swap
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
            arr_t[j][i], arr_t[j + 1][i] = arr_t[j + 1][i], arr_t[j][i]
            # 행 열 열
            mx = max(mx, count(arr[i]), count(arr_t[j]), count(arr_t[j + 1]))

            # 복구
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
            arr_t[j][i], arr_t[j + 1][i] = arr_t[j + 1][i], arr_t[j][i]

    return mx


n = int(input())
arr = [list(input()) for _ in range(n)]
arr_t = list(map(list, zip(*arr)))

ans = max(solve(arr, arr_t), solve(arr_t, arr))
print(ans)
