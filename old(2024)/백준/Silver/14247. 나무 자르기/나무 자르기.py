# 나무가 빨리 자라는 순으로 뒤늦게 자르면 됨.

n = int(input())

# 나무 길이와 자라는 속도 zip
heights = list(map(int, input().split()))
speeds = list(map(int, input().split()))

# 자라는 속도 기준 정렬
trees = list(zip(heights, speeds))
trees.sort(key=lambda x:x[1])

# 나무 자르기
tree_sum= 0
for day in range(n):
    tree_sum += trees[day][0]+ trees[day][1]*(day)

# 출력
print(tree_sum)