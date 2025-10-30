# 입력
N, K = map(int, input().split())
A_lst = list(map(int, input().split()))

#
cnt =0

res = -1

# 선택 정렬
for i in range(N-1,0,-1):
    max_idx = i
    for j in range(i+1):
        if A_lst[max_idx] < A_lst[j]:
            max_idx = j
    if max_idx != i :
        cnt+=1
        A_lst[i], A_lst[max_idx] = A_lst[max_idx], A_lst[i]
        if cnt == K:
            res = A_lst
            break

if res== -1:
    print(-1)
else :
    print(*res)

