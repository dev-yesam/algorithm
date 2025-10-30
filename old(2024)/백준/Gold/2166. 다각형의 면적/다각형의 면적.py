import sys

input = sys.stdin.readline

## 신발끈 공식 써야함

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
total_temp = 0
lst.append(lst[0])
for i in range(n):
    total_temp += lst[i][0]*lst[i+1][1] - lst[i][1]*lst[i+1][0]

total_ans = abs(total_temp)/2
print(round(total_ans, 2))
