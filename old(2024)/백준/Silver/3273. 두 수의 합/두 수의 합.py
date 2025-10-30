n = int(input())
lst = list(map(int, input().split()))
lst.sort()
x = int(input())

start, end = 0, n - 1
cnt = 0

while start < end:
    sum_num = lst[start] + lst[end]

    if sum_num > x:
        end -= 1

    elif sum_num == x:
        cnt += 1
        start += 1

    else:
        start += 1

print(cnt)
