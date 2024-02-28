list_num = []
while(True):
    num = int(input())
    if num == 0:
        break
    list_num.append(num)

list_dital = []
for x in list_num:
    cnt = 0
    temp = 0
    while(True):
        temp += x%10
        x = x//10
        if x == 0:
            list_dital += [temp]
            break
for x in list_dital:
    print(x)


