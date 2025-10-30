# 20115 에너지 드링크

# 입력
n = int(input())
drinks = list(map(int,input().split()))


# 최댓값 계산
drink_max = max(drinks)

# 나머지 값 계산, 합의 1/2 하기
drinks.remove(drink_max)
half_rest = sum(drinks)/2

print(drink_max + half_rest)