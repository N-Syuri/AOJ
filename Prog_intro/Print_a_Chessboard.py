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
        if x%2 == 0:
           for y in range(int(list[2*i+1])):
              if(y%2 == 0):
                  w.append("#")
              else:
                  w.append(".")
        else:
           for y in range(int(list[2*i+1])):
              if(y%2 == 0):
                  w.append(".")
              else:
                  w.append("#")
        result = "".join(w)
        print(result)
    print()