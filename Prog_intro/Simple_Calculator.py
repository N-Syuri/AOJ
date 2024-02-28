list = []
while(True):
   line = input().split()
   a = int(line[0])
   op = line[1]
   b = int(line[2])
   if(op == "+"):
      list.append(int(a + b))
   elif(op == "-"):
      list.append(int(a - b))
   elif(op == "*"):
      list.append(int(a * b))
   elif(op == "/"):
      list.append(int(a / b))
   elif(op == "?"):
      for i in list:
         print(i)
      break

