# 11399

# 사람의 수 입력 받기
N = int(input())

# 인출 시간 입력 받기
withdraw = list(map(int, input().split()))

# 인출 시간 작은 순으로 정렬
withdraw.sort()

# 시간 계산 하기
withdraw_sum = 0
final_sum = 0
for i in withdraw:
    withdraw_sum += i
    final_sum += withdraw_sum

print(final_sum)