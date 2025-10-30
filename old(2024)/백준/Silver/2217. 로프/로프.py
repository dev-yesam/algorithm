# 2217
import sys

# 입력
n = int(sys.stdin.readline())
lst = []
for i in range(n):
    s = int(sys.stdin.readline())
    lst.append(s)

# 무게 내림차순 정렬
lst.sort(reverse=True)

# 들 수 있는 무게 계산
cnt = 0   # 지금까지 로프 개수
weights = 0 # 현재 로프로 들 수 있는 무게
max_weight = 0 # 로프로 들 수 있는 최대 무게

# 로프로 들 수 있는 무게 = 제일 약한 로프가 버틸 수 있는 무게 * 총 로프 개수
for i in lst:
    cnt +=1
    weights = i * cnt
    # 최대값 갱신
    if weights > max_weight:
        max_weight = weights

# 출력
print(max_weight)

