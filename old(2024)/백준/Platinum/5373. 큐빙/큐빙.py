## 아이디어
# 6개 가운데 애들 위치는 고정
# 8개의 모서리
# 12개의 그 사이 모서리

# 1. 단순무식하게 6면을 다 넣어서 푸는 법
# - 가운데 고정이니까, 6면 리스트로 해두고,
# - 아님 3차원 배열로 해두고, 각각의 블록 정보를 기억해놓는 건?
# - 그 블록의 방향 정보도 기록해 둔다면 괜찮을 듯함.
# 2. 윗면만 넣어서 푸는 법


import sys

input = sys.stdin.readline

t = int(input())
for tc in range(t):
    n = int(input())  # 큐브를 돌리는 횟수
    methods = input().rstrip().split()  # 큐브 돌리는 방법
    # 큐브 배열 6개 면
    # 인덱스 U[0], D[1], F[2], B[3], L[4], R[5]
    arr = [[['w', 'w', 'w'] for _ in range(3)], [['y', 'y', 'y'] for _ in range(3)],
           [['r', 'r', 'r'] for _ in range(3)], [['o', 'o', 'o'] for _ in range(3)],
           [['g', 'g', 'g'] for _ in range(3)], [['b', 'b', 'b'] for _ in range(3)]]

    for method in methods:
        if method[0] == 'U':
            if method[1] == '+':
                # 현재 면 90도 회전
                arr[0] = [list(row) for row in zip(*arr[0][::-1])]
                # 나머지 4면 수정
                # F->L->B->R->F
                temp = arr[2][0][::]
                arr[2][0] = arr[5][0][::]  # R->F
                arr[5][0] = arr[3][0][::]  # B->R
                arr[3][0] = arr[4][0][::]  # L->B
                arr[4][0] = temp[::]  # F(temp)-> L
            else:
                # 현재 면 -90도 회전
                arr[0] = [list(row) for row in zip(*arr[0])][::-1]
                # 나머지 4면 수정 F -> R -> B -> L -> F
                temp = arr[2][0][::]
                arr[2][0] = arr[4][0][::]
                arr[4][0] = arr[3][0][::]
                arr[3][0] = arr[5][0][::]
                arr[5][0] = temp[::]
        elif method[0] == 'D':
            if method[1] == '+':
                # 현재 면 90도 회전
                arr[1] = [list(row) for row in zip(*arr[1][::-1])]
                # 나머지 4면 수정 F -> R -> B -> L -> F
                temp = arr[2][2][::]
                arr[2][2] = arr[4][2][::]
                arr[4][2] = arr[3][2][::]
                arr[3][2] = arr[5][2][::]
                arr[5][2] = temp[::]
            else:
                # 현재 면 -90도 회전
                arr[1] = [list(row) for row in zip(*arr[1])][::-1]
                # 나머지 4면 수정 F->L->B->R->F
                temp = arr[2][2][::]
                arr[2][2] = arr[5][2][::]  # R->F
                arr[5][2] = arr[3][2][::]  # B->R
                arr[3][2] = arr[4][2][::]  # L->B
                arr[4][2] = temp[::]  # F(temp)-> L
        elif method[0] == 'F':
            if method[1] == '+':
                # 현재 면 90도 회전
                arr[2] = [list(row) for row in zip(*arr[2][::-1])]
                # 나머지 4면 수정 U->R->D->L->U
                temp = arr[0][2][::]
                arr[0][2] = [arr[4][i][2] for i in range(3)][::-1]
                for i in range(3):
                    arr[4][i][2] = arr[1][2][2 - i]
                arr[1][2] = [arr[5][i][0] for i in range(3)]
                for i in range(3):
                    arr[5][i][0] = temp[i]
            else:
                # 현재면 -90도 회전
                arr[2] = [list(row) for row in zip(*arr[2])][::-1]
                # 나머지 4면 수정 U->L->D->R->U
                temp = arr[0][2][::]
                arr[0][2] = [arr[5][i][0] for i in range(3)]
                for i in range(3):
                    arr[5][i][0] = arr[1][2][i]
                arr[1][2] = [arr[4][i][2] for i in range(3)][::-1]
                for i in range(3):
                    arr[4][i][2] = temp[2 - i]
        elif method[0] == 'B':
            if method[1] == '+':
                # 현재 면 90도 회전
                arr[3] = [list(row) for row in zip(*arr[3][::-1])]
                # 나머지 4개 면 회전 U->L->D->R->U
                temp = arr[0][0][::]
                arr[0][0] = [arr[5][i][2] for i in range(3)]
                for i in range(3):
                    arr[5][i][2] = arr[1][0][i]
                arr[1][0] = [arr[4][i][0] for i in range(3)][::-1]
                for i in range(3):
                    arr[4][i][0] = temp[2 - i]
            else:
                # 현재 면 -90도 회전
                arr[3] = [list(row) for row in zip(*arr[3])][::-1]
                # 나머지 4개 면 회전 U<-L<-D<-R<-U
                temp = arr[0][0][::]
                arr[0][0] = [arr[4][i][0] for i in range(3)][::-1]
                for i in range(3):
                    arr[4][i][0] = arr[1][0][2 - i]
                arr[1][0] = [arr[5][i][2] for i in range(3)]
                for i in range(3):
                    arr[5][i][2] = temp[i]
        elif method[0] == 'L':
            if method[1] == '+':
                # 현재 면 90도 회전
                arr[4] = [list(row) for row in zip(*arr[4][::-1])]
                # 나머지 4개면 회전 U<-B<-D<-F<-U
                temp = [arr[0][i][0] for i in range(3)]
                for i in range(3):
                    arr[0][i][0] = arr[3][2 - i][2]
                for i in range(3):
                    arr[3][i][2] = arr[1][i][2]
                for i in range(3):
                    arr[1][i][2] = arr[2][2 - i][0]
                for i in range(3):
                    arr[2][i][0] = temp[i]
            else:
                # 현재 면 -90도 회전
                arr[4] = [list(row) for row in zip(*arr[4])][::-1]
                # 나머지 4개면 회전 U<-F<-D<-B<-U
                temp = [arr[0][i][0] for i in range(3)]
                for i in range(3):
                    arr[0][i][0] = arr[2][i][0]
                for i in range(3):
                    arr[2][i][0] = arr[1][2 - i][2]
                for i in range(3):
                    arr[1][i][2] = arr[3][i][2]
                for i in range(3):
                    arr[3][i][2] = temp[2 - i]
        elif method[0] == 'R':
            if method[1] == '+':
                # 현재 면 90도 회전
                arr[5] = [list(row) for row in zip(*arr[5][::-1])]
                # 나머지 4개 면 회전 U<-F<-D<-B<-U
                temp = [arr[0][i][2] for i in range(3)]
                for i in range(3):
                    arr[0][i][2] = arr[2][i][2]
                for i in range(3):
                    arr[2][i][2] = arr[1][2 - i][0]
                for i in range(3):
                    arr[1][i][0] = arr[3][i][0]
                for i in range(3):
                    arr[3][i][0] = temp[2 - i]
            else:
                # 현재 면 -90도 회전
                arr[5] = [list(row) for row in zip(*arr[5])][::-1]
                # 나머지 4개면 회전 U<-B<-D<-F<-U
                temp = [arr[0][i][2] for i in range(3)]
                for i in range(3):
                    arr[0][i][2] = arr[3][2 - i][0]
                for i in range(3):
                    arr[3][i][0] = arr[1][i][0]
                for i in range(3):
                    arr[1][i][0] = arr[2][2 - i][2]
                for i in range(3):
                    arr[2][i][2] = temp[i]
    # 출력하기
    for i in range(3):
        print(''.join(arr[0][i]))
