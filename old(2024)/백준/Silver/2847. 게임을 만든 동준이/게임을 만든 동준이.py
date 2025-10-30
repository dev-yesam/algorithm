

# 총 N 개의 레벨 입력 받기
N = int(input())
levels = [] #레벨을 담을 빈 리스트
for _ in range(N):
    level = int(input())
    levels.append(level)

# 레벨 높은 순부터 낮은 순으로 순회하며 이전보다 작아지게 만들기
    
levels.reverse() # 역순으로 재배치
cnt = 0
for i in range(1,len(levels)):
    if levels[i] >= levels[i-1]:
        minus = levels[i] - levels[i-1]+1
        levels[i] -= minus
        cnt += minus


# 출력
print(cnt)
