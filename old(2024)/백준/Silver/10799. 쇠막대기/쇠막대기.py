
ans = 0

stack = []

num_open = 0

loc = input()

for i in range(len(loc)):

    if loc[i] == "(":
        stack.append(i)

    elif loc[i] == ')':

        # 레이저냐 아니냐.
        if loc[i-1] == "(":
            stack.pop()
            ans += len(stack)

        else:
            stack.pop()
            ans += 1

print(ans)
# 3 4 4 2 3 1 2 1 1 1 1 1
