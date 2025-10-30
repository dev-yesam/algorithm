k = int(input())
stack = []
for i in range(k):

    elem = int(input())
    if elem == 0:
        stack.pop()
    else:
        stack.append(elem)


print(sum(stack))
