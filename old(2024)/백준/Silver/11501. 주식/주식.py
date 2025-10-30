# 11501

# 입력
import sys
t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    days = list(map(int, sys.stdin.readline().split()))
    
    # 날짜 역순 변환
    days.reverse()

    # 이익의 합
    res = 0

    # 최대값
    max = 0

    # 날짜 순회
    for day in days:
        if day > max:
            max = day
        else:
            res += max - day
    
    # 출력
    print(res)