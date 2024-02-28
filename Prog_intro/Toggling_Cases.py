str_line = input()
char_text = list(str_line)
list_text = []
for x in str_line:
    if x >= "A" and x <= "Z":
        list_text.append(x.lower())
    elif x >= "a" and x <= "z":
        list_text.append(x.upper())
    else:
        list_text.append(x)
print("".join(list_text))
