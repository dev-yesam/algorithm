import sys

input = sys.stdin.readline
# 입력
N = int(input())
A_lst = list(map(int, input().split()))
B_lst = list(map(int, input().split()))

# 선택 정렬
for i in range(N - 1, 0, -1):
    if A_lst == B_lst:
        break

    largest = i
    for j in range(i):
        if A_lst[j] > A_lst[largest]:
            largest = j
    A_lst[i], A_lst[largest] = A_lst[largest], A_lst[i]

print(1 if A_lst ==B_lst else 0)