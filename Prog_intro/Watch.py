a = int(input())
h_t = 3600
m_t = 60
c_t = 60
h = int(a/h_t)
m = int((a - 3600*h)/m_t)
c = (a - 3600*h - 60*m)%c_t
print(h,m,c,sep = ":")