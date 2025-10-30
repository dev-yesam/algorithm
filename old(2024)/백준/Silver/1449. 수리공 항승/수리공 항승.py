#1449

n, l = map(int, input().split())

locations = list(map(int, input().split()))
locations.sort()
location = locations[0]
cnt = 1

for idx in range(1, len(locations)):
    if locations[idx] <= location+l-1:
        pass
    else:
        location = locations[idx]
        cnt+=1

print(cnt)

    