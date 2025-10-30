n, k = map(int, input().split())
nums = list(map(int, input().split()))


each = 0
# k개를 더해주기(초기값인듯)
for i in range(k):
    each += nums[i]
maxv = each

# 다음 인덱스 더해주고, 이전 인덱스 빼주기
# k-1에서 끝났으니까 k부터 시작
for i in range(k,n):
    each += nums[i]
    each -= nums[i-k]
    maxv = max(maxv, each)

print(maxv)
