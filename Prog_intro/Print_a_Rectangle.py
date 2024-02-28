list = []
while(True):
    H,W = map(int,input().split())
    if H == 0 and W == 0:
        break
    list.append(H)
    list.append(W)

for i in range(int(len(list)/2)):
    for x in range(int(list[2*i])):
        w = []
        for y in range(int(list[2*i + 1])):
            w.append("#")
        result = "".join(w)
        print(result)
    print()

