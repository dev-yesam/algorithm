T = int(input())
for tc in range(T):

    N = input()

    a_num = N.count('(')
    b_num = N.count(')')

    cnt = 0
    answer ='YES'
    if a_num==b_num:
        for i in N:
            if i =="(":
                cnt +=1
            if i == ")":
                cnt -=1

            if cnt <0 :
                answer = 'NO'


        print(answer)
    else:
        print("NO")