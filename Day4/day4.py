import numpy as np
with open("data.txt", 'r') as file:
    lines = file.readlines()

data = np.array([list(line.strip()) for line in lines])
data = np.pad(data, ((0,3),(0,3)), 'constant')
print(data)
#----------------------------1------------------------------

filter1=np.array(['X','M','A','S']).flatten()
filter2=np.array(['S','A','M','X']).flatten()

def check_filter(x,y):
    count= 0
    hori  = data[y, x:x+4]
    verti = data[y:y+4, x]
    digi_1  = data[[y, y+1, y+2, y+3],[x, x+1, x+2, x+3 ]] 
    digi_2  = data[[y+3, y+2, y+1, y],[x, x+1, x+2, x+3 ]]

   
    if np.array_equal(filter1, hori) or np.array_equal(filter2, hori):
        count+=1       
    if np.array_equal(filter1, verti) or np.array_equal(filter2, verti):
        count+=1      
    if np.array_equal(filter1, digi_1) or np.array_equal(filter2, digi_1):
        count+=1       
    if np.array_equal(filter1, digi_2) or np.array_equal(filter2, digi_2):
        count+=1
    return count

global_count = 0
for r in range(len(data)-3):
    for c in range(len(data[0])-3):
        global_count += check_filter(c,r)
print(global_count)

#----------------------------2------------------------------
filterx1=np.array(['M','A','S','M','A','S']).flatten()
filterx2=np.array(['M','A','S','S','A','M']).flatten()
filterx3=np.array(['S','A','M','M','A','S']).flatten()
filterx4=np.array(['S','A','M','S','A','M']).flatten()


def check_for_x(x,y):
    x_pattern = data[[y, y+1, y+2,y+2, y+1, y],[x, x+1, x+2, x, x+1, x+2]]
    if np.array_equal(filterx1, x_pattern) or np.array_equal(filterx2, x_pattern) or np.array_equal(filterx3, x_pattern) or np.array_equal(filterx4, x_pattern):
           return 1
    return 0

global_count = 0
for r in range(len(data)-2):
    for c in range(len(data[0])-2):
        global_count += check_for_x(c,r)
print(global_count)
