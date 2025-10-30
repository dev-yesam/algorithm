

N, S = map(int, input().split())

lst = list(map(int, input().split()))
cnt =0
for i in range(1, 1<<N):
    l=[]
    for j in range(N):
        if i & (1<<j):
            l.append(lst[j])
    if sum(l) ==S:
        cnt +=1

print(cnt)


