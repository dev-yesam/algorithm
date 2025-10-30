# 입력 받기

A, B = input().split()


# 1. 최댓값 => 5를 전부 6으로 보는 경우

lst_A = list(A) # 문자열 리스트화
lst_B = list(B)

for i in range(len(lst_A)): 
    if lst_A[i]=='5':
        lst_A[i] ='6'
    
    Max_A = ''.join(lst_A)  # A 최댓값
    Max_A = int(Max_A)

for i in range(len(lst_B)): 
    if lst_B[i]=='5':
        lst_B[i] ='6'
    
    Max_B = ''.join(lst_B)  # B 최댓값
    Max_B = int(Max_B)



# 2. 최솟값 : 6을 전부 5로 보는 경우

lst_A = list(A) # 문자열 리스트화
lst_B = list(B)

for i in range(len(lst_A)): 
    if lst_A[i]=='6':
        lst_A[i] ='5'
    
    Min_A = ''.join(lst_A)  # A 최솟값
    Min_A = int(Min_A)    
for i in range(len(lst_B)): 
    if lst_B[i]=='6':
        lst_B[i] ='5'
    
    Min_B = ''.join(lst_B)  # B 최솟값
    Min_B = int(Min_B)

# 최솟값과 최댓값 출력
print(Min_A + Min_B, Max_A + Max_B)