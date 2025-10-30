# 입력
n = int(input())

# 2진수 변화
bin_n = bin(n)

# 역순으로 순회하며, 3의 거듭제곱해서 더하기
multi = 1
res = 0
for i in bin_n[-1:1:-1]:
    res += multi * int(i)
    multi *= 3

# 출력
print(res)