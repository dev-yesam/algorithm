n = int(input())  # 1~

d = [0] * (n + 3)

d[1] = 0
d[2] = 1
d[3] = 1

for i in range(4, n + 1):
    c1 = d[i - 1] + 1
    c2 = d[i // 2] + 1 if i % 2 == 0 else 10 ** 6
    c3 = d[i // 3] + 1 if i % 3 == 0 else 10 ** 6
    d[i] = min(c1, c2, c3)

print(d[n])
