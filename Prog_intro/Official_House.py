cnt = int(input())
list_room = []
building = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
i = 0

while i != cnt:
    temp = [int(x) for x in input().split()]
    list_room.append(temp)
    i += 1

for x in range(16):
    if x%4 == 3:
        for z in range(20):
            building[x].append("#")
    else:
        for z in range(10):
            building[x].append(0)

def floor(buliding_room:list,f:list):
    buliding_room[f[2]-1] += f[3]

def floor_sel1(f:list):#floor is first_list [1 2 3 4]
    floor(building[4*(f[0]-1) + f[1]-1],f)
        
for floor_1 in list_room:#list-in-list number
    floor_sel1(floor_1)

for f_num,room in enumerate(building):
    if f_num%4 == 3:
        if f_num != 15:
           print("".join(map(str,room)))
    else:
        print(" ",end="")
        print(" ".join(map(str,room)))
