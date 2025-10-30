from collections import deque

n = int(input())
cards = deque()
for card in range(1,n+1):
    cards.append(card)

# 카드가 1개 남을 때까지 or 카드가 다 없어질 때까지 그리고 그 마지막 카드를 기록.
while cards:

    # 제일 위의 카드 버리기
    ans = cards.popleft()
    # 카드가 남아있다면?
    if not cards:
        break
    # 제일 위의 카드를 맨 밑으로 넣기
    cards.append(cards.popleft())

print(ans)

