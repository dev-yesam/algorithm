#1541

# 입력
import sys
s = sys.stdin.readline().rstrip()

# - 기준으로 split
s_lst=s.split('-')

# 뒤에 뺄 값들을 담아둘 리스트
s_minus_list= []
for i in s_lst[1:]:
    j=i.split('+')
    s_minus_list.extend(j)
    
# 첫번재 - 앞 숫자를 모두 합해줌
s_plus = sum(map(int, s_lst[0].split('+')))

# 첫번째 - 뒤 숫자를 모두 합해줌
s_minus = sum(map(int, s_minus_list))

# 빼주고 출력하면 됨.
print(s_plus - s_minus)