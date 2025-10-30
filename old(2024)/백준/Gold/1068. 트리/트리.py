n = int(input())
lst = list(map(int, input().split()))
x = int(input())


# 노드 지우기
def dfs(x):
    lst[x] = -2

    for i in range(n):
        # 부모가 x인 i가 있다면?
        if lst[i] == x:
            dfs(i)
dfs(x)

# 리프노드 개수 세기
# -2가 아니면서, 해당 인덱스가 lst에 없어야함.
cnt = 0
for i in range(n):
    if lst[i] != -2 and i not in lst:
        cnt += 1

print(cnt)
