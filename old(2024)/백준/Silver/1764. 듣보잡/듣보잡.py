# 1764

# 사람의 수 입력
n, m = map(int,input().split())

# 세트 생성
n_set = set()
m_set = set()

# 명단 입력 받으며, 각 세트에 추가
for _ in range(n):
    n_set.add(input())

for _ in range(m):
    m_set.add(input())

# 교집합 세트 구하기
inter_set = n_set & m_set

# 리스트화 및 정렬
lst = list(inter_set)
lst.sort()

#출력
print(len(lst))
for i in lst:
    print(i)

