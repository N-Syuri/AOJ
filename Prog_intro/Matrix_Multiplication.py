n,m,l = map(int,input().split())
list_a = []
list_b = []
list_b1 =[]
cnt_a = 0
cnt_b = 0
while(True):
    if cnt_a == n:
        break
    cnt_a+=1
    list_a += [[int(x) for x in input().split()]]

while(True):
    if cnt_b == m:
        break
    cnt_b+=1
    list_b += [[int(x) for x in input().split()]]


for y in range(l):
   list_b1 += [[x[y] for x in list_b]]

list_result = []

for v1 in list_a:
    for v2 in list_b1:
       list_result += [sum([x*y for x,y in zip(v1,v2)])]

res = []
for x in list_result:
    res = [[group] for group in zip(*[iter(list_result)]*l)]


new_list = [[*item] for sublist in res for item in sublist]

for x in new_list:
   print(" ".join(map(str,x)))
