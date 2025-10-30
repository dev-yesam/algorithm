# 1. 자주 나올수록
# 2. 길이가 길수록
# 3. 알파벳 앞일 수록
# 길이는 m 이상

import sys
input = sys.stdin.readline

# 입력
n, m = map(int, input().split())
words = dict()
for _ in range(n):
    word = input().rstrip()
    if len(word)>=m:
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1


# 단어 - 개수쌍 리스트
words_set = list(words.items())
words_set.sort(key = lambda x : (-x[1], -len(x[0]), x[0]) )

# 출력
for i  in words_set:
    print(i[0])