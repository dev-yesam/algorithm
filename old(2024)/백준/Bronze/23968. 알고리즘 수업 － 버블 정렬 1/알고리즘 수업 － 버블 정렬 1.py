n, k = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0
for i in range(n-1,0,-1):
    for j in range(i):
        if lst[j]>lst[j+1]:
            cnt +=1
            lst[j], lst[j+1] = lst[j+1], lst[j]
            if cnt == k:
                print(lst[j], lst[j+1])
                exit()

if cnt < k:
    print(-1)