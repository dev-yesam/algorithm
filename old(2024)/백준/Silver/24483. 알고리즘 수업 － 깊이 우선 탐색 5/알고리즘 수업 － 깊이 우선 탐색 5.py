import sys
n, m, r = map(int, input().split())
sys.setrecursionlimit(n+10)

adjl = [[] for _ in range(n + 1)]
depth = [-1] * (n + 1)
orders = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    adjl[a].append(b)
    adjl[b].append(a)

for node in adjl:
    node.sort()



def dfs(now, d):
    global order, total
    depth[now] = d
    orders[now] = order
    total += depth[now] * orders[now]

    order += 1

    for next in adjl[now]:
        if orders[next] == 0:
            dfs(next, d + 1)


total = 0
order = 1

dfs(r, 0)

# for i in range(1, n + 1):
#     # print(f'{i}번 노드 => depth: {depth[i]} order: {orders[i]}')
#     total += depth[i] * orders[i]

print(total)