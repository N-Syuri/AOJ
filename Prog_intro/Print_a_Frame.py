list = []
while(True):
    H,W = map(int,input().split())
    if H == 0 and W == 0:
        break
    list.append(H)
    list.append(W)
for i in range(int(len(list)/2)):
    for x in range(list[2*i]):
        w = []
        if x == 0 or x == list[2*i]-1:
            for y in range(list[2*i+1]):
               w.append("#")
            result = "".join(w)
            print(result)
        else:
            w.append("#")
            for y in range(list[2*i+1]-2):
                w.append(".")
            w.append("#")
            result = "".join(w)
            print(result)
    print()