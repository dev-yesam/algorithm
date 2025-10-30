#20310

# 입력
s = list(input())


# 1 개수 파악 및 제거
cnt1 = int(s.count('1')/2)
for _ in range(cnt1):
    s.remove('1')


# 0 개수 파악 및 제거
cnt0 = int(s.count('0')/2)
#remove 함수는 앞에서부터 제거하기에, 역순으로 변환
s.reverse()
for _ in range(cnt0):
    s.remove('0')

#다시 원래대로 전환
s.reverse()


#출력
print(''.join(s))

