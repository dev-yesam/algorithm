t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    lst = [0] * 201
    answer = -1
    for _ in range(n):
        start, end = map(int, input().split())
        start, end = (start+1) // 2, (end+1) // 2
        if start > end:
            start, end = end, start
        for s in range(start, end + 1):
            lst[s] += 1

    answer = max(lst)
    print(f'#{tc}', answer)