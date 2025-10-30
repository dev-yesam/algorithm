n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

answer = []
visited = [0] * (n + 1)


def backtrack(lst, level):
    if level == m:
        print(*answer)
        return

    prev = 0
    for idx in range(n):
        if lst[idx] == prev or visited[idx]:
            continue
        prev = lst[idx]
        answer.append(lst[idx])
        visited[idx] = 1
        backtrack(lst, level + 1)
        answer.pop()
        visited[idx] = 0


backtrack(lst, 0)
