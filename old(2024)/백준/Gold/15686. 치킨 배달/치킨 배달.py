n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
# 각 치킨 집마다 모든 거리
chick_lst = []
house_lst = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            house_lst.append((i, j))

        elif arr[i][j] == 2:
            chick_lst.append((i, j))


chick_num = len(chick_lst)
house_num = len(house_lst)

chick_house = [[100] * house_num for _ in range(chick_num)]

for chick in range(chick_num):
    for house in range(house_num):
        chick_house[chick][house] = abs(chick_lst[chick][0] - house_lst[house][0]) + abs(chick_lst[chick][1] - house_lst[house][1])



############ 조합 구하기 ##############
# chick_num개의 치킨 집에서 m개의 치킨 집을 고르는 경우의 수


chick_idx_lst = [i for i in range(chick_num)]
temp = []
cmbs = []  # 조합들 들어갈 리스트

def run(lev, start):
    if lev == m:
        cmbs.append(temp[:])

        return

    for i in range(start, chick_num):
        temp.append(chick_idx_lst[i])
        run(lev+1, i+1)
        temp.pop()

run(0,0)


############# 치킨집 조합에서 최소갑 구하기 ############
ans = 10000

for com in cmbs:
    cnt = 0
    for house_idx in range(house_num):
        min_house = 100
        for com_c in com:
            min_house = min(min_house, chick_house[com_c][house_idx])

        cnt += min_house

    if ans > cnt:
        ans = cnt

print(ans)


