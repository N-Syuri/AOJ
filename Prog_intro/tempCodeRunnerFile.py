import sys
list_char = []
cnt = 0

while(True):
    try:
       str_line = input().lower()
       list_char += str_line
    except:
        break

dict = {}
dict["a"] = 0
dict["b"] = 0
dict["c"] = 0
dict["d"] = 0
dict["e"] = 0
dict["f"] = 0
dict["g"] = 0
dict["h"] = 0
dict["i"] = 0
dict["j"] = 0
dict["k"] = 0
dict["l"] = 0
dict["m"] = 0
dict["n"] = 0
dict["o"] = 0
dict["p"] = 0
dict["q"] = 0
dict["r"] = 0
dict["s"] = 0
dict["t"] = 0
dict["u"] = 0
dict["v"] = 0
dict["w"] = 0
dict["x"] = 0
dict["y"] = 0
dict["z"] = 0
list_alp = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for x in list_char:
    if x >= "a" and x <= "z":
       dict[x] += 1

for x in list_alp:
    print(f"{x} : {dict[x]}")