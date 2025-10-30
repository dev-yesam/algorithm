T = int(input())

for i in range(T):
    Q = 0
    D = 0
    N = 0
    P = 0

    M = int(input())

    Q = M // 25
    M = M % 25

    D = M // 10
    M = M % 10

    N = M // 5
    M = M % 5

    P = M // 1

    print(Q, D, N, P)