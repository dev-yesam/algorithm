# 1의 숫자는 앞이 0이어야만 생길 수 있음
# 0의 숫자는 앞이 1 또는 0이면 생길 수 있음
n = int(input())

dp_z = [0] * (n+1)
dp_o = [0] * (n+1)
dp_o[1] = 1

for i in range(2,n+1):
    dp_z[i] = dp_z[i-1] + dp_o[i-1]
    dp_o[i] = dp_z[i-1]

print(dp_z[n]+dp_o[n])