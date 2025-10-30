import sys
input = sys.stdin.readline

n = int(input())
s = input().rstrip()
stack = []

alpha = {}
for i in range(n):
    alpha[chr(65+i)] = int(input())


for tk in s:

    if tk in '*/+-':
        if tk == '*':
            new = stack.pop(-2) *stack.pop()
            stack.append(new)
        elif tk == '/':
            new = stack.pop(-2) / stack.pop()
            stack.append(new)
        elif tk == '+':
            new = stack.pop(-2) + stack.pop()
            stack.append(new)
        elif tk == '-':
            new = stack.pop(-2) - stack.pop()
            stack.append(new)


    else:
        stack.append(alpha[tk])

ans = stack.pop()
print("%0.2f"%ans)