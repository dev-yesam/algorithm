# 2039

lst = []
for _ in range(9):
    n = int(input())
    lst.append(n)

# 선택 정렬

for i in range(8):
    min_idx = i
    for j in range(i + 1, 9):
        if lst[min_idx] > lst[j]:
            min_idx = j
    lst[min_idx], lst[i] = lst[i], lst[min_idx]

# 완전 탐색 (제외할 2명 찾기)
for i in lst:
    for j in lst:
        if i != j and sum(lst) - i-j == 100:
            lst.remove(i)
            lst.remove(j)
            break

# 출력
for i in lst:
    print(i)
