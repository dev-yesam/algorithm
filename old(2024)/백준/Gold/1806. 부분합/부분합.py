n, s = map(int, input().split())
lst = list(map(int, input().split()))

start = end = 0
length = n  # 초기값

if sum(lst) < s:
    print(0)

else:
    total = lst[0]
    while start<= end < n :
        if total >= s:
            # 길이 갱신 가능하냐
            if length > end - start + 1:
                length = end - start + 1
            total -= lst[start]
            start += 1

        else:
            end += 1
            if end < n:
                total += lst[end]
    print(length)
