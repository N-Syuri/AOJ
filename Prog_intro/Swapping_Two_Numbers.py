list_val = []
flag = 0
loopend = 0
while(True):
    val = input()
    values = [int(x) for x in val.split()]
    
    for val in values:
      if val == 0:
          if flag == 0:
              list_val.append(val)
              flag = 1
          elif flag == 1:
              list_val.append(val)
              loopend = 1
              break
      else:
          flag = 0
          list_val.append(val)
    if loopend == 1:
        break

#print(list_val[:-2])
#print(len(list_val)/2)
while(True):
    for i in range(int(len(list_val)/2)-1):
        if(list_val[2*i] > list_val[2*i+1]):
           list_val[2*i],list_val[2*i+1] = list_val[2*i+1],list_val[2*i]
        print(f"{list_val[2*i]} {list_val[2*i+1]}")
    break

