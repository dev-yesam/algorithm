#13417 

# 입력
t = int(input())

# 케이스 반복
for _ in range(t):
    n = int(input())

    cards = input().split()
    card_list = []

    # ord 함수를 이용하여, 비교.
    start=cards[0]

    for card in cards:
        # 리스트 첫번째 요소보다, 작다면 왼쪽 삽입
        if ord(card) <= ord(start):
            card_list.insert(0, card)
            start = card
        # 만약 아니라면, 오른쪽 삽입
        else:
            card_list.append(card)

    # 리스트 문자열 변환
    card_str = ''.join(card_list)
    print(card_str)