val = int(input())
r_list = []
i = 1
while(i <= val):
    x = i
    x = int(x)
    if(x%3==0):
        r_list.append(str(i))
    else:
        while(x != 0):
          if x%10 == 3:
            r_list.append(str(i))
            break
          else:
            x = int(x/10)
            
    i+=1

result = " ".join(r_list)
print(f" {result}")
