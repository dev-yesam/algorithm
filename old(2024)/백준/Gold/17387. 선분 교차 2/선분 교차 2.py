## 더 간단하게 줄일 수 있을 것 같은데 아직 잘 모르겠음.

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
A = (x1, y1)
B = (x2, y2)
C = (x3, y3)
D = (x4, y4)


def ccw(A, B, C):
    result = (A[0] * B[1] - A[1] * B[0]) + (B[0] * C[1] - B[1] * C[0]) + (C[0] * A[1] - C[1] * A[0])
    if result > 0:
        return 1  # CCW
    elif result < 0:
        return -1  # CW
    else:
        return 0


def is_between(A, B, C):
    if min(A[0], B[0]) <= C[0] <= max(A[0], B[0]) and (min(A[1], B[1]) <= C[1] <= max(A[1], B[1])):
        return True
    return False


ABC, ABD = ccw(A, B, C), ccw(A, B, D)
CDA, CDB = ccw(C, D, A), ccw(C, D, B)

# 그냥 선분 교차
if ABC * ABD == -1 and CDA * CDB == -1:
    print(1)


# 4점이 일직선인 경우
elif ABC == 0 and ABD == 0 and CDA == 0 and CDB == 0:
    if is_between(C,D,A) or is_between(C, D, B) or is_between(A,B,C) or is_between(A,B,D):
        print(1)
    else:
        print(0)

    # 3점이 일직선인 경우
elif ABC * ABD == 0 or CDA * CDB == 0:
    if ABC * ABD <= 0 and CDA * CDB <= 0:
        print(1)
    else:
        print(0)

# 안 겹치는 경우
else:
    print(0)
