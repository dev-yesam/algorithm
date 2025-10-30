n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

res = 0

for i in range(n):
    res += max(A)*min(B)
    A.remove(max(A))
    B.remove(min(B))

print(res)