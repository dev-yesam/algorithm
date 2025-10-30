# 1946

# 입력
n, m = map(int, input().split())
cards = list(map(int, input().split()))

# 오름차순 정렬
cards.sort()

# 반복 돌리며 합치기
for _ in range(m):
    sum_cards = cards[0] + cards[1]
    cards[0], cards[1] = sum_cards, sum_cards
    cards.sort()

# 결과값 출력
print(sum(cards))
