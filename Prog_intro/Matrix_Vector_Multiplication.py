a,b = map(int,input().split())
list_A = []
list_B = []
list_temp = []
list_result = []

for x in range(a):
    list_A += [[int(x1) for x1 in input().split()]]
for y in range(b):
    list_B += [int(input())]

for x in range(a):
    for y in range(b):
       list_temp = [int(A*B) for A,B in zip(list_A[x],list_B)]
       result = sum(list_temp)
    list_result += [result]


"".join(map(str,list_result))
for x in range(a):
    print(list_result[x])