import pandas as pd
# Daten laden
data = pd.read_csv('data.txt', sep="\s+", header=None)
#------------------------------------#

left = sorted(data[0].tolist())
right = sorted(data[1].tolist())

count_1 = 0
for l, r in zip(left, right):
    count_1 += abs(l - r)
print(count_1)

#------------------------------------#
count_2 = 0

for l in left:
    count_2 += + l * right.count(l)
print(count_2)