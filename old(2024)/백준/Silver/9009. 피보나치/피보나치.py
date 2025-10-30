# 9009

# 입력 받기
t= int(input())

for _ in range(t):
    n = int(input())
    
    # 피보나치 수열 담을 빈 리스트
    lst=[]
    # 피보나치 수열 
    b=1
    c=0

    # 피보나치 수열로 반복 돌리며 최대일 때 빼기
    while True:
        a= b+c
        if n<a:
            lst.append(b)
            n-=b
            if n==0:
                break
            #피보나치 초기화
            b=1
            c=0
        #피보나치 다음항
        else:
            c=b
            b=a
    #역순으로 출력
    for i in lst[::-1]:
        print(i, end=' ')
    print()
