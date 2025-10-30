t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    lst = [input() for _ in range(n)]
    cnt = 0
    # 1) 부분집합
    for i in range(1, 1 << n):
        cmp = (1 << 26) - 1
        temp_num = 0
        for j in range(n):
            if i & (1 << j):
                for w in lst[j]:
                    if 'a' <= w <= 'z':
                        temp_num = temp_num | 1 << (ord(w) - ord('a'))
        if temp_num == cmp:
            cnt += 1

    print(f'#{tc}', cnt)
