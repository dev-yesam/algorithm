n = int(input())
sequence = list(map(int, input().split()))

# 1. 정렬하기
sequence.sort()

# 2. 지금까지 더한 것보다, 이후 숫자가 1차이보다 크다면? 연결안됨
total = 0
for elem in sequence:
    if elem > total + 1:
        break
    total += elem

print(total + 1)
