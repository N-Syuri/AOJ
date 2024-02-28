score_list = []
Grade_list = []
while(True):
    a,b,c = map(int,input().split())
    if a == -1 and b == -1 and c == -1:
        break
    score_list += [[a,b,c]]

for score in score_list:
    if score[0] == -1 or score[1] == -1:
       Grade_list.append("F")
    elif (score[0] + score[1]) >= 80:
        Grade_list.append("A")
    elif (score[0] + score[1]) < 80 and (score[0] + score[1]) >= 65:
        Grade_list.append("B")
    elif (score[0] + score[1]) < 65 and (score[0] + score[1]) >= 50:
        Grade_list.append("C")
    elif (score[0] + score[1]) < 50 and (score[0] + score[1]) >= 30:
        if score[2] >= 50:
            Grade_list.append("C")
        else:
            Grade_list.append("D")
    else:
        Grade_list.append("F")
"".join(Grade_list)
for g in Grade_list:
    print(g)
    
