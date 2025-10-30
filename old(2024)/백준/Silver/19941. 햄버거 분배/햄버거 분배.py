n, k = map(int, input().split())
s = list(input())
cnt = 0
for i in range(len(s)):
    if s[i] == 'P':
        for j in range(max(0, i-k), min( i+k+1    ,len(s))):
            if s[j] == 'H':
                cnt+=1
                s[j]= 0
                break
print(cnt)
