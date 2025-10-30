# 추가 게임은 적을수록, #승률 추가는 1개만 높으면 됨.


games, wins = map(int, input().split())

rate1 = int(wins * 100 / games)

start = 0
end = 1e9

answer = -1

while start <= end:
    if rate1 == 99:
        break

    mid = (start + end) // 2

    # 승률
    rate2 = int(((wins + mid) * 100) // (games + mid))

    if rate2 > rate1:
        end = mid - 1
        answer = mid
    else:
        start = mid + 1

print(int(answer))
