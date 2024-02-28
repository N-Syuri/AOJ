list_num = []
while(True):
    n,x = map(int,input().split())
    if n == 0 and x == 0:
        break
    else:
        list_num += [[n,x]]

result = 0
for x in list_num:
    for y in range(1,x[0]):
        for y1 in range(y+1,x[0]):
            for y2 in range(y1+1,x[0]+1):
                if x[1] - y2 - y1 - y == 0:
                    result += 1
    print(result)
    result = 0