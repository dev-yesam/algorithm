
n = int(input())
bin_n = bin(n).replace('0b', '')

cnt = bin_n.count('1')

print(cnt)