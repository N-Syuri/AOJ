values = input().split()
integer_list = [int(x) for x in values]
s = sorted(integer_list)
print(*s)