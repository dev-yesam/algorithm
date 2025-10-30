# k번째 교환되는 수 = 오름차순 정렬일 때 k-1 인덱스의 원소.
n, k = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0 # 교환 횟수

for i in range(n-1, 0,-1):
    max_idx = i
    for j in range(0,i):
        if lst[max_idx] < lst[j] :
            max_idx = j
    if max_idx != i:
        lst[i], lst[max_idx] = lst[max_idx], lst[i]
        cnt += 1
        if cnt == k:
            print(lst[max_idx], lst[i])
            break
if cnt < k:
    print(-1)