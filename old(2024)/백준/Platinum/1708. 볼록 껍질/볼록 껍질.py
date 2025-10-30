import sys
input = sys.stdin.readline


def ccw(a,b,c):
    result = (a[0]*b[1]-a[1]*b[0])+(b[0]*c[1]-b[1]*c[0])+(c[0]*a[1]-c[1]*a[0])
    return result

n = int(input())
lst = [tuple(map(int, input().split())) for _ in range(n)]
lst.sort(key=lambda x:(x[0],x[1]))
temp_cw = []
temp_ccw = []

for i in lst:
    while True:
        if len(temp_cw) < 2:
            temp_cw.append(i)
            break
        if ccw(temp_cw[-2], temp_cw[-1], i) < 0:
            temp_cw.append(i)
            break
        else:
            temp_cw.pop()

for i in lst:
    while True:
        if len(temp_ccw) < 2:
            temp_ccw.append(i)
            break
        if ccw(temp_ccw[-2], temp_ccw[-1], i) > 0:
            temp_ccw.append(i)
            break
        else:
            temp_ccw.pop()

result = temp_cw + temp_ccw[1:-1]
print(len(result))



