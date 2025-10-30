# 10828
import sys
input = sys.stdin.readline

stack = []



# 입력
n =int(input())
for i in range(n):

    dir =input().strip()

    if dir == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)

    elif dir == 'size':
        print(len(stack))

    elif dir == 'empty':
        if stack:
            print(0)
        else:
            print(1)

    elif dir == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)

    else:
        a, b = dir.split()
        if a == 'push':
            stack.append(int(b))


