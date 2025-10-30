# 1. 처음 양 숫자에 계속 += 한 뒤에,
# 2. 각 자리 수마다 가져와서 있는지 없는지 확인
# 3. 0~9 다 있게 되면 종료. 그때의 양 번호 출력


t = int(input())
for tc in range(1, t + 1):
    start_n = int(input())
    now_n = 0
    cpr = (1 << 10) - 1
    now_digits = 0

    while now_digits != cpr:
        now_n += start_n
        # 각 자리수가 있으면 추가해주는 것
        for digit in str(now_n):
            now_digits = now_digits | (1 << int(digit))

    print(f'#{tc}', now_n)
