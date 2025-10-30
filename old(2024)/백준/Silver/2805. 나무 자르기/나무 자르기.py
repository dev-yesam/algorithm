# 2512

# 입력
n,m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

# 자를 길이

start=0
end = max(lst)

while start<=end:
    k = 0

    mid = (start+end)//2

    for tree in lst:
        if tree >= mid:
            k += tree-mid

        else:
            pass

    if k >=m:
        res = mid
        start = mid +1

    else:
        end = mid -1

print(res)
