# k개의 수를 골라 집합 만들어 놓고
# 거기서 6개만 뽑는 것.
# 조합 문제네.

def recur(level, start):
    # 종료 조건
    if level == 6:
        print(*res)
        return

    # 재귀 호출
    for i in range(start,k):
        res.append(lst[i])
        recur(level+1,i+1)
        res.pop()

while True:
    lst = list(map(int, input().split()))
    k = lst.pop(0)
    if k == 0: break

    res = []
    recur(0,0)
    print()