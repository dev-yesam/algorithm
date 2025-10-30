n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))

res= []
# 같은 수 여러번 가능
# 수열 중복 x
# 비내림차순

# 함수
def recur(num, start):
    # 종료 조건 num == m
    if num==m:
        print(*res)
        return

    # 재귀호출
    prev = 0
    for i in range(start,n):
        if prev != lst[i]:
            prev = lst[i]
            res.append(lst[i])

            recur(num+1, i)
            # 원상복구
            res.pop()

recur(0,0)
