import numpy as np
import itertools

with open("data.txt", 'r') as file:
    txt = file.read().splitlines()

matrix = np.array([list(line) for line in txt])
pad_size = 300
matrix = np.pad(matrix, pad_size , mode='constant', constant_values='.')
count_matrix = matrix.copy()

distinct_chars = set(char for row in matrix for char in row if char != '.')

count = 0
print(matrix)
for c in distinct_chars:
    i, j = np.where(matrix == c)
    pos = [(int(x), int(y)) for x, y in zip(i, j)] #alle positionen vom char

    combinations = list(itertools.combinations(pos, 2)) #alle Kombinationen dieser positionen
    for pair in combinations:

        print(f"pair: {pair}")

        dif = ((pair[0][0] - pair[1][0]),(pair[0][1] - pair[1][1])) 

        p1 = (pair[0][0] - dif[0],pair[0][1]-dif[1])
        p2 = (pair[1][0] - dif[0],pair[1][1]-dif[1])
        p3 = (pair[0][0] + dif[0],pair[0][1]+dif[1])
        p4 = (pair[1][0] + dif[0],pair[1][1]+dif[1])
        print(p1,p2,p3,p4)
        if matrix[p1] != c: count_matrix[p1] = '#' 
        if matrix[p2] != c: count_matrix[p2] = '#'
        if matrix[p3] != c: count_matrix[p3] = '#' 
        if matrix[p4] != c: count_matrix[p2] = '#'

   
   
    
count_matrix= count_matrix[pad_size:-pad_size, pad_size:-pad_size]  
print(count_matrix)
     
count = np.count_nonzero(count_matrix == '#')   
print(count)