n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))

# 중복해서 뽑아도 됨.
# 수열이 중복되면 안됨.

res= []

def recur(num):
    if num == m :
        print(*res)
        return

    # 중복만 안되게.
    prev = 0
    for i in lst:
        if prev != i:
            prev = i
            res.append(i)
            recur(num+1)
            res.pop()

recur(0)
