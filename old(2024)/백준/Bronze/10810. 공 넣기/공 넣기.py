# 10810 공 넣기

# N 입력. 1~N 적힌 바구니
# M 공 넣는 횟수. 범우 정하고 같은 숫자 공 넣음.
# 최종적으로 각 바구니 어떤 공이 남아있는가.


# 입력
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 바구니 배열 생성
n_lst = [0] * n

# 공 넣기
for _ in range(m):
    i, j, k = map(int, input().split())
    for ball in range(i-1, j):
        n_lst[ball] = k

# 출력
print(*n_lst)
