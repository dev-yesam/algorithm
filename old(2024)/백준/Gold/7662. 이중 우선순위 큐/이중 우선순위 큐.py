# 240408
# BOJ 7662

# 우선순위 큐 2개 + 세트 자료형으로 삭제한 인덱스 확인

from heapq import heappush, heappop
import sys
input = sys.stdin.readline  # 아오 이거 해줘야하는듯. input이 많아서.

t = int(input())
for tc in range(t):
    k = int(input())  # 연산의 개수
    max_h = []
    min_h = []
    del_idx = set() # 삭제한 인덱스 번호
    for idx in range(k):
        opr, num = input().split()
        num = int(num)
        if opr == 'I':
            heappush(min_h, (num, idx))
            heappush(max_h, (num * -1, idx))

        else:
            if num == -1:  # 최소힙에서 pop
                while min_h:
                    temp = heappop(min_h)
                    if temp[1] in del_idx:
                        continue
                    del_idx.add(temp[1])
                    break

            else:  # 최대힙에서 pop
                while max_h:
                    temp = heappop(max_h)
                    if temp[1] in del_idx:
                        continue
                    del_idx.add(temp[1])
                    break

    max_ans = min_ans = 0
    max_flag = min_flag = False

    # 최솟값과 최댓값 찾기

    while max_h:
        temp = heappop(max_h)
        if temp[1] in del_idx:
            continue
        # del_idx.add(temp[1])  => 이걸 할 필요가 없었음.
        max_flag = True
        max_ans = temp[0] * -1
        break

    while min_h:
        temp = heappop(min_h)
        if temp[1] in del_idx:
            continue
        min_flag = True
        min_ans = temp[0]
        break

    if min_flag and max_flag:
        print(max_ans, min_ans)
    else:
        print("EMPTY")
