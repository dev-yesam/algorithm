from collections import deque

n = int(input())
lst = list(map(int, input().split()))
ans = deque()



# 새로 쌓아진 카드는 1~ N
# 원래 쌓여 있던 카드들 => ans

for i in range(1, n+1):
    if lst[i*-1] == 1:
        ans.appendleft(i) # 제일 위에 올려 놓으면 된다.

    elif lst[i*-1] == 2:
        # 위에서 두번째에 올려 놓는다
        temp = ans.popleft()
        ans.appendleft(i)
        ans.appendleft(temp)
    else:
        # 제일 바닥에 놓는다.
        ans.append(i)

print(*ans)
