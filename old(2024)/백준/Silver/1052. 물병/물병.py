# 1052

n, k = map(int, input().split())

# 1의 수 세기
count_ones = bin(n).count('1')

# 줄여야 할 물병의 수
bottles_to_reduce = count_ones - k

if bottles_to_reduce <= 0:
    print(0)

else:
    answer =0
    power= 0
    while bottles_to_reduce > 0:
        # 계속 1이 있으면 그만큼 더해서 bottle_to_reduce 가 0보다 작거나 같아질때가지 만듦.
        if n & (1<<power):
            n += (1<<power)
            answer+= (1<<power)
            bottles_to_reduce = bin(n).count('1') - k
        power += 1

    print(answer)
