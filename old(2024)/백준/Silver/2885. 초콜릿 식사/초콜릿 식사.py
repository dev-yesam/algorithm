# 2885

# 입력
import sys

k = int(sys.stdin.readline().rstrip())

# 크기 측정
n = 0
while True:
    if k <= 2**n:
        break
    else:
        n += 1

max_n = n

# 2의 거듭제곱으로 계속 빼기
while True:
    if k >= 2**n:
        k -= 2**n

    else:
        if k == 0:
            break
        else:
            n -= 1

min_n = n

# 출력
print(2**max_n, max_n - min_n)
