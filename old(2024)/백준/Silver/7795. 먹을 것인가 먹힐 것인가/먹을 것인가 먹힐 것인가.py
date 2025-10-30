T = int(input())
for _ in range(T):
    A_num, B_num = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort()

    total = 0
    for a in A:
        start = 0
        end = B_num - 1
        idx = -1
        while start <= end:
            mid = (start + end) // 2

            if a > B[mid]:
                start = mid + 1
                idx = mid
            else:
                end = mid - 1

        if idx != -1:
            total += (idx + 1)
        else:
            break

    print(total)
