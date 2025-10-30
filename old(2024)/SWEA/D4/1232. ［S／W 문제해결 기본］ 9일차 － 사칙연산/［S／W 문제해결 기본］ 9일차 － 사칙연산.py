# 중위 순회
def inorder(x):
    if 0 < x <= n + 1:

        a = inorder(left[x])
        p = tree[x]
        b = inorder(right[x])

        if p == '+':
            return a + b
        elif p == '-':
            return a - b
        elif p == '*':
            return a * b
        elif p == '/':
            return a / b

        # 노드가 숫자이면
        else:
            p = int(p)
            return p


t = 10
for tc in range(1, t + 1):
    # 입력
    n = int(input())

    # 이진 트리 생성
    # - 루트 번호 1
    tree = [0] * (n + 1)
    right = [0] * (n + 1)
    left = [0] * (n + 1)

    # 이진 트리 입력
    for i in range(n):
        lst = input().split()
        p = int(lst.pop(0))
        tree[p] = lst.pop(0)
        if lst:
            left[p] = int(lst.pop(0))
            right[p] = int(lst.pop(0))

    # 중위 순회해서 루트 노드 출력
    print(f'#{tc}', int(inorder(1)) )
