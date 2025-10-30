numbers, b = input().split()
b = int(b)
n = len(numbers)

ans = 0

for i in range(n):

    if numbers[n-i-1].isdigit():
        ans += int(numbers[n-i-1]) * (b ** i)
    else:
        ans += (ord(numbers[n-i-1]) - ord('A') + 10) * (b ** i)

print(ans)
