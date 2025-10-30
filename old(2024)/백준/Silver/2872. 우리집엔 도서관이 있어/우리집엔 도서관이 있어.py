import sys

# 입력
n = int(sys.stdin.readline())
books = []
for _ in range(n):
    books.append(int(sys.stdin.readline().rstrip()))



# 최대 비교

idx = books.index(n)
now_book = n-1

for book in books[:idx][::-1]:
    if book == now_book:
        now_book -= 1
        pass


print(now_book)
        



