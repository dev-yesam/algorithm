n, m = map(int,input().split())
lst = sorted(list(map(int, input().split())))

res = []

def recur(num, start_idx):
    if num == m:
        print(*res)
        return

    for idx in range(start_idx, n):
        res.append(lst[idx])
        recur(num+1, idx)
        res.pop()

recur(0,0)