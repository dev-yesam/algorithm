# 백준 0128

# 입력
n = int(input())
# 브론즈 -> 다이아 등급 기준액 입력
s,g,p,d = map(int, input().split())
# MVP 등급 및 최대금액을 담을 리스트
rank = input()
prev = 0
total = 0
# 3개월
# 30 60 90 150
# B S G

# 랭크 순회하며 최대 금액 탐색
for i in rank:
    if i == 'B':
        prev = s - prev -1
    elif i == 'S':
        prev = g - prev -1
    elif i == 'G':
        prev = p - prev -1
    elif i == 'P':
        prev = d - prev -1
    else: #다이아일 때는 그냥 다이아 기준액만큼이 최대값임
        prev = d
    total += prev

# 출력
print(total)

        

