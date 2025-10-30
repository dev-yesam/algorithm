#1931

# 회의의 수 입력
N = int(input())

# 각 회의 정보 입력
m_list = [] 
for i in range(N):
    # (a, b) 시작시간, 종료시간
    a,b = map(int, input().split())
    m_list.append((a,b))

#끝나는 시간순으로 정렬
sorted_list = sorted(m_list, key = lambda x : (x[1],x[0]))

#회의 배치 및 첫 시간 넣기
final_list = []
final_list.append(sorted_list[0])

# (c, d) 시작시간, 종료시간
for i in range(1,len(sorted_list)):
    if sorted_list[i][0] >= final_list[-1][1]:
        final_list.append(sorted_list[i])

# 회의 최대 개수 출력
print(len(final_list))


