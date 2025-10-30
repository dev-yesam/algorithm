# 직사각형 정보 주어짐
# x1, y1, x2,y2
# 2차원 카운트 배열

for _ in range(4):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())

    # [1] 공통 부분이 없음
    if x2 < x3 or y2 < y3  or x1 > x4 or y1 > y4 :
        print('d')

    # [2] 점 또는 선
    elif x1==x4 or y1 == y4 or x2==x3 or y2==y3:
        # [2-1] 점
        if (x1==x4 and y1==y4) or (x1==x4 and y2==y3) or (x2==x3 and y2==y3) or (x2==x3 and y1==y4):
            print('c')

        # [2-2] 선
        else:
            print('b')

    # [3] 직사각형
    else:
        print('a')