#1439

# 문자열 입력 받기
S= input()

# 문자열 중복 제거
lst = []
lst.append(S[0])

for i in range(1,len(S)):
    if S[i] != lst[-1]:
        lst.append(S[i])

# 0과 1중 적은 개수 확인
if lst.count('0') <= lst.count('1'):
    print(lst.count('0'))
else:
    print(lst.count('1'))
    


