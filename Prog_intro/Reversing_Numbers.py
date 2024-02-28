a = int(input())
list_val = [x for x in input().split()]
result = []
for item in reversed(list_val):
    result.append(item)
res = " ".join(result)
print(res)