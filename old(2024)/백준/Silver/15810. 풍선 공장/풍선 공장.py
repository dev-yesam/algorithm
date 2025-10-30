staff_num, balloon_num = map(int,input().split())
balloons = list(map(int, input().split()))

# 이진 탐색
start = 0
# end = 1000000
end = max(balloons) * balloon_num

ans = 1e12
while start <= end:
    time = (start+end)//2

    balloon_res = 0
    for balloon in balloons:
        balloon_res += (time // balloon)

    # 만약 시간이 너무 길어서 너무 많이 만들었다면
    if balloon_res >= balloon_num:
        end = time - 1
        ans = time
    else:
        start = time +1

print(ans)