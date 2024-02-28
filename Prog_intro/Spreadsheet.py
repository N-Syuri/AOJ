r,c = map(int,input().split())
list_add = []
list_val = []
cnt = 0
while(True):
    list_val += [[int(x) for x in input().split()]]
    cnt+=1
    if cnt == r:
        break

for x in list_val:
    x += [sum(x)]

def list_addition(v1:list,v2:list) -> list:
    result = [x+y for x,y in zip(v1,v2)]
    return result

re = []
for x in range(c + 1):
    re += [0]

for x in list_val:
    re = list_addition(x,re)

list_val += [re]
" ".join(map(str,list_val))
for x in list_val:
    print(*x)