# 25166

# 아리 돈 1111111111(2) = 1023 원
# 아리는 1~1023 모두 표현 가능

# 입력
S, M = map(int,input().split())

# 'No thanks'
if S <= 1023:
    print("No thanks")

# 'Thanks' and 'Impossible'
if S >= 1024:
    if (S - 1023) & ~M:
        print('Impossible')

    else:
        print("Thanks")




