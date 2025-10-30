#16953

# sys 연습
import sys

# 입력
A, B = sys.stdin.readline().split()

# B를 반복 돌리기

cnt = 1
while True:
    if int(A)>int(B):
        print(-1)
        break
    elif int(A) == int(B):
        print(cnt)
        break
    elif str(B)[-1]== '1':
        B = str(B)[:-1]
        cnt+=1
    elif int(B)%2==0:
        B = int(int(B)/2)
        cnt+=1
    else:
        print(-1)
        break

