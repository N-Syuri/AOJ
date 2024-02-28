def print_card(card:list):
    for x in card:
        suit,card_num = x
        print(suit,card_num) 


val = int(input())
i = 0
card_set = []
while(i != val):
    suits,card_val = map(str,input().split())
    card = [suits,int(card_val)]
    card_set.append(card)
    i+=1
complete_cardset = []
for c in range(13):
    S_set = ["S",c+1]
    complete_cardset.append(S_set)
    H_set = ["H",c+1]
    complete_cardset.append(H_set)
    C_set = ["C",c+1]
    complete_cardset.append(C_set)
    D_set = ["D",c+1]
    complete_cardset.append(D_set)
miss = [tuple(card) for card in set(map(tuple,complete_cardset)) - set(map(tuple,card_set))]

S_Set = []
H_Set = []
C_Set = []
D_Set = []
for card in miss:
    suit = card[0]
    if suit =="S":
        S_Set.append(card)
    if suit =="H":
        H_Set.append(card)    
    if suit =="C":
        C_Set.append(card)
    if suit =="D":
        D_Set.append(card)

S_Set.sort(key=lambda x:x[1])
H_Set.sort(key=lambda x:x[1])
C_Set.sort(key=lambda x:x[1])
D_Set.sort(key=lambda x:x[1])

print_card(S_Set)
print_card(H_Set)
print_card(C_Set)
print_card(D_Set)