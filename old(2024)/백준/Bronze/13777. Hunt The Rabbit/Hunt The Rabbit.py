# rabbit

while True:

    rabbit = int(input())

    if rabbit ==0:
        exit()

    # we must add 1 because of index.
    envelopes = [i+1 for i in range(50)]

    # binary search
    start=0
    end = 49


    # list of middles
    lst = []

    while start <= end:
        middle = (start + end) // 2
        lst.append(middle+1)
        if envelopes[middle] == rabbit:
            break
        elif envelopes[middle] < rabbit:
            start = middle+1
        else:
            end = middle-1

    # print
    print(*lst)