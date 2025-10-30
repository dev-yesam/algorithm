from collections import deque
n, k = map(int, input().split())
lst = list()
q = deque()
for num in range(1, n+1):
    q.append(num)

while q:
    for _ in range(k-1):
        q.append(q.popleft())
    lst.append(q.popleft())

ans = ', '.join(map(str, lst))
print('<'+ans+">")
