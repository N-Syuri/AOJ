W = input()
W = W.lower()
T = []
while(True):
    temp = input().split()
    if temp == ['END_OF_TEXT']:
        break
    T += temp
list_t = []
for t in T:
    temp = t.lower()
    list_t.append(temp)
cnt = 0

for x in list_t:
    if x == W:
        cnt += 1
print(cnt)