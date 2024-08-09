import sys
input = sys.stdin.readline

# n 이 10만? nlogn 정도는 됨. 160만이니까.

chingho_num, character_num = map(int, input().split())
chingho_lst = []
for _ in range(chingho_num):
    chingho, power = input().split()
    power = int(power)
    chingho_lst.append((chingho, power))

for _ in range(character_num):

    character_power = int(input())

    # 이진 탐색
    start = 0
    end = chingho_num-1
    ans = 0
    while start <= end:
        mid = (start + end) // 2
        if chingho_lst[mid][1] >= character_power:
            end = mid - 1
            ans = mid
        else:
            start = mid + 1

    print(chingho_lst[ans][0])



