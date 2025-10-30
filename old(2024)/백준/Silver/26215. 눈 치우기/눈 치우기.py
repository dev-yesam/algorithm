# 26125

# 최대 칸 수 만큼 정렬해서 계속 줄이면 될 것 같음.

house_num = int(input())
snows = list(map(int, input().split()))
snows.sort(reverse=True)
cnt = 0

while snows[0] > 0:
    cnt += 1

    if house_num >= 2:
        snows[0] -= 1

        if snows[1] > 0:
            snows[1] -= 1

        snows.sort(reverse=True)
    else:
        cnt = snows[0]
        break

if cnt <= 1440:
    print(cnt)
else:
    print(-1)
