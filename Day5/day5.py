import numpy as np
with open("data2.txt", 'r') as file:
    txt = file.read().splitlines()

#--------------------1-----------------------
top = txt[:(txt.index(""))]
top = [tuple(line.split('|')) for line in top]

bottom = txt[(txt.index("")):]
bottom.pop(0)

count = 0
mistakes = []
for b in bottom:
    b=b.split(",")
    b = list(reversed(b))
    rules = []
    for i in range(len(b)): #für jedes update
        for j in range(i + 1, len(b)):  #Kreuzprodukt für alle i<j
            if i < j:  
                rules.append((b[i],b[j]))
    print(rules)
    if not(any(map(lambda v: v in rules, top ))):
        count += int(b[len(b) // 2])
print(count)
#--------------------2-----------------------


