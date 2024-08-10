## 이전 코드 속도 테스트

# 중위표기식 입력
word = input()

# 출력할 후위 표기식
postfix =''

# 스택
stack = list()
# 후위 표기식 전환
for token in word:

    # 연산자일 때?
    if token in '()+-*/':
        # '(' 얘는 계산에서 가장 먼저 해야할 애라서, 무조건 스택에 넣어줌
        if token == '(':
            stack.append(token)
        # ')' 얘는 이제 계산 마무리해야해서, 스택에 있는 연산 다 빼서 postfix에 붙여줌.
        # '(' 얘 나올 때까지 빼주고 괄호는 걍 없애줌.
        elif token == ')':
            while stack[-1] != '(':
                postfix += stack.pop()
            # '('얘는 걍 없애줌
            stack.pop()
        # +와 -는 우선 순위 낮은 애들이라, 안에 곱하기 같은 게 있으면 그걸 빼줘야함. 즉 계산 시켜야함.
        # */ 뿐 아니라 다른 + -도 먼저 빼서 계산 시켜야함.
        # 즉 stack에 '(' 나오거나 빌때까지 빼줘야함.
        # '('는 ')'나올 때까지는 둬야지.
        elif token == '+' or token == '-':
            # 스택이 비어있다면?
            if not stack:
                stack.append(token)
            # 스택에 뭐가 들어있다면?
            else:
                while stack and stack[-1] != '(':
                    postfix += stack.pop()
                stack.append(token)
        elif token == '*' or token =='/':
            # 스택이 비어있다면?
            if not stack:
                stack.append(token)
            # 스택에 뭐가 들어 있다면?
            # +-는 들어 있어도 상관 없음
            # */는 빨리 계산 되어야 하니까 빼줘야함.
            else:
                while stack and stack[-1] in '*/':
                    postfix += stack.pop()
                stack.append(token)

    # 피연산자 일때?
    else:
        postfix += token

# 스택에 남아있는 거 처리
while stack:
    postfix += stack.pop()

# 출력
print(postfix)