n, m = map(int, input().split())

# 백트래킹.
res = []
visited = [0] * (n + 1)


def recur(num,start):

    # 2. 종료조건
    if num == m:
        print(*res)
        return

    # 3. 재귀호출
    for i in range(start, n + 1):
        if not visited[i]:
            visited[i] = 1
            res.append(i)
            recur(num + 1,i+1)

            # 복구
            res.pop()
            visited[i] = 0

recur(0,1)
