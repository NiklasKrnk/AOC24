import pandas as pd
data = pd.read_csv("data.txt", header=None)

#----------------1---------------#
def check(rep):
    return all(3 >= r[i] - r[i+1] >= 1  for i in range(len(r)-1)) or all(-1 >= r[i] - r[i+1] >= -3  for i in range(len(r)-1))

errors = []
count = 0
for r in data[0]:
    r = list(map(int, r.split()))
    if check(r): 
        count += 1
    else: 
        errors.append(r)
print(count)

#----------------2---------------#
count = 0

def is_safe_with_removal(r):
    for i in range(len(r)):
        modified_r = r[:i] + r[i+1:]
        if all(3 >= modified_r[j] - modified_r[j+1] >= 1 for j in range(len(modified_r) - 1)) or \
           all(-1 >= modified_r[j] - modified_r[j+1] >= -3 for j in range(len(modified_r) - 1)):
            return True
    return False

for r in data[0]:
    r = list(map(int, r.split()))
    if check(r):
        count += 1
    elif is_safe_with_removal(r):
        count += 1
print(count)
