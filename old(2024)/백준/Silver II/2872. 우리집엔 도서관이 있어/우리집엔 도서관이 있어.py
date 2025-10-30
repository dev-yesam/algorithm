# 책 빼서 가장 위에 놓는 것만 가능.

import sys

input = sys.stdin.readline
n = int(input())

books = [int(input()) for _ in range(n)]

# 가장 큰 수 찾고, 그 전까지 내림차순이어야하는데, 아닌거 나오면 바로 그 수만큼 옮겨야함.
big_idx = books.index(n)
big_num = n
small_num =n-1


for idx in range(big_idx-1,-1,-1):
    if books[idx] == small_num:
        big_num = small_num
        small_num -= 1

print(small_num)

