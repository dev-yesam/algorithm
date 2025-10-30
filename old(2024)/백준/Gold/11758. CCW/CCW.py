A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))


result1 = A[0]*B[1] + B[0]*C[1] + C[0]*A[1]
result2 = A[1]*B[0] + B[1]*C[0] + C[1]*A[0]
if result1-result2 > 0:
    print(1)
elif result1-result2 < 0:
    print(-1)
else:
    print(0)