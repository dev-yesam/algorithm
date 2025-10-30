from collections import deque
import sys

input = sys.stdin.readline

q = deque()
n = int(input())
for _ in range(n):

    dir = input().rstrip().split()

    if dir[0] == 'push':
        q.append(int(dir[1]))

    elif dir[0] == 'pop':
        print(q.popleft() if q else -1)

    elif dir[0] == 'size':
        print(len(q))

    elif dir[0] == 'empty':
        print(0 if q else 1)

    elif dir[0] == 'front':
        print(q[0] if q else -1)

    elif dir[0] == 'back':
        print(q[-1] if q else -1)
