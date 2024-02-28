W,H,x,y,r = map(int,input().split())
r_ed_cir = x-r
l_ed_cir = x+r
t_ed_cir = y+r
b_ed_cir = y-r
#print(r_ed_cir,l_ed_cir,t_ed_cir,b_ed_cir)
if(r_ed_cir >= 0 and l_ed_cir <= W and t_ed_cir <= H and b_ed_cir >= 0):
    print("Yes")
else:
    print("No")