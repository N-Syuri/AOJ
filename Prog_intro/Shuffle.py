str_list = []
shuffle_num = []
while(True):
    str_li = input().split()
    if str_li == ["-"]:
        break
    str_list += str_li 
    num = int(input())
    for x in range(num):
        shuffle_num += [input()]
print(str_list)
print(shuffle_num)