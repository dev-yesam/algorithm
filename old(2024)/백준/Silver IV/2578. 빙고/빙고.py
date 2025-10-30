arr = [list(map(int, input().split())) for _ in range(5)]
lst = [list(map(int, input().split())) for _ in range(5)]
cnt = 0
for i in range(5):
    find_bingo = False
    for j in range(5):
        num = lst[i][j]

        # 빙고 표시
        for k in range(5):
            if num in arr[k]:
                arr[k][arr[k].index(num)]=0
                cnt += 1
                break
        # 빙고 확인
        bingo = 0
        ## 가로 빙고
        for k in range(5):
            if all(x==0 for x in arr[k]):
                bingo += 1
        ## 세로 빙고
        for k in range(5):
            if all(arr[l][k]==0 for l in range(5)):
                bingo += 1
        ## 대각 빙고
        if all(arr[k][k] == 0 for k in range(5)):
            bingo += 1
        if all(arr[k][5-k-1] == 0 for k in range(5)):
            bingo += 1

        if bingo >= 3:
            find_bingo = True
            break

    if find_bingo:
        break

print(cnt)