import re
with open("data.txt", "r") as file:
    txt = file.read()
#---------------------1--------------------------#
def mul(x,y):
    return x*y
x = re.findall(r"mul\(\d{0,3},\d{0,3}\)", txt)
print(f"count {sum(eval(i) for i in x)}")

#---------------------2--------------------------#
while(True):
    match = re.search(r"don't\(\)(?:(?!do\(\)).|\s)*do\(\)", txt)
    if not match: break
    txt = txt[:match.start()] + txt[match.end():]
x2 = re.findall(r"mul\(\d{0,3},\d{0,3}\)", txt)
print(f"count 2 {sum(eval(i) for i in x2)}")
