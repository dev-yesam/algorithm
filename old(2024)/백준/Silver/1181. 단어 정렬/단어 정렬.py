# 1181

# 입력
n = int(input())
lst = []
for _ in range(n):
    lst.append(input())

# 중복 제거
lst = list(set(lst))

# 정렬
lst.sort(key= lambda x: (len(x), x))

# 출력
for i in lst:
    print(i)