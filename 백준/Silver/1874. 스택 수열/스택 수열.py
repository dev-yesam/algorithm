import sys

input = sys.stdin.readline
ans =[]
n = int(input())
stack = []
answer = True
start= 1
for _ in range(n):
    num = int(input())

    while start <= num:
        stack.append(start)
        ans.append('+')
        start += 1

    if stack[-1] == num:
        stack.pop()
        ans.append('-')
    else:
        answer = False

if not answer:
    print('NO')
else:
    for l in ans:
        print(l)

