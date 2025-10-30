# 1052 물병

# 입력
N, K = map(int, input().split())

# 2진수로 바꾼 현재 물병의 수(2진수 1의 수)
water_bottle = bin(N).count('1')

new = N  # 이후 물병의 총 수(10진수)
cnt = 0  # 추가할 물병의 총 수(10진수)
bottle = 0  # 추가할 물병
while bin(new).count('1') > K:
    bottle = 2 ** bin(new)[::-1].index('1')
    new += bottle
    cnt += bottle

print(cnt)
