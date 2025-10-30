# 2512

# 입력
n = int(input())
lst = list(map(int, input().split()))
lst.sort()
budget = int(input())

# 모두 배정 가능
if sum(lst) <= budget:
    cutline = max(lst)

# 모두 배정 불가
else:
    sum_lst = 0
    for i in range(n):
        cutline = (budget - sum_lst) // (n - i)

        if cutline >= lst[i]:
            sum_lst += lst[i]
            continue
        else:
            break

print(int(cutline))
