# 1515

# 수 입력 받기 (문자열)
lst = list(input())



# lst가 다 빌 때까지 루프
n=0
while lst :
    n += 1
    for i in str(n):
        if not lst:
            break
        if lst[0] == i:
            lst.pop(0)


print(n)       