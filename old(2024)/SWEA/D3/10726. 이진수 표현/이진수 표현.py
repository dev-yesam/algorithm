t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())

    ans = 'OFF'
    if m & ((1<<n)-1) == (1<<n)-1:
        ans = 'ON'

    print(f'#{tc}', ans)