# 입력
# k : 최대 버틸 수 있는 무게
cats_num, k = map(int, input().split())

cats = list(map(int, input().split()))

# 작은 고양이 선택 -> 큰 무게에서 내려오며 k 이하 되면 끝
cats.sort()
cnt = 0
small_idx =0
big_idx = cats_num - 1

while small_idx < big_idx:

    if cats[small_idx] + cats[big_idx] <= k:
        cnt +=1
        small_idx+=1
        big_idx -= 1
    else:
        big_idx -= 1


print(cnt)