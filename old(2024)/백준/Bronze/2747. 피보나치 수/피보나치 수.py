n = int(input())

d = [0] * (n+1)

def fibo(x):
    # 종료 조건
    if x == 0:
        return 0

    if x == 1 :
        return 1

    # dp 테이블에 저장되어있다면?
    if d[x]:
        return d[x]

    # 저장 안 되어 있다면
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(n))