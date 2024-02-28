list_val = []
while True:
    val = int(input())
    if val == 0:
        break
    list_val.append(val)
#print(list_val)
y = 1
for x in list_val:
    if x == 0:
        break   
    print(f"Case {y}: {x}")
    y+=1