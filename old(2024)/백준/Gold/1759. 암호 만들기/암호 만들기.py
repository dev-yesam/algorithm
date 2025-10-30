# 비트 연산자로 부분 집합 구해서 푸는 방법
# 조합보다 훨신 편하고 나을 때가 있는 듯.

# 입력
L, C = map(int, input().split())


vowel_lst = ['a', 'e', 'i', 'o', 'u']
lst = input().split()
lst.sort()

# L 자리 암호 만들기
res = []
for i in range(2**C):

    # L 자리인가
    if bin(i).count('1') != L:
        continue

    temp=[]
    v_cnt = 0 # 모음 수 확인용
    for j in range(C):
        if i & (1<<j):
            temp.append(lst[j])
            if lst[j] in vowel_lst:
                v_cnt += 1

    # 모음 수가 맞는가.
    if 1<= v_cnt <= L-2:
        res.append(''.join(temp))

# 출력
res.sort()
for ans in res:
    print(ans)




