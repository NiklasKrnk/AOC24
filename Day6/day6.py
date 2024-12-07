import numpy as np
import matplotlib.pyplot as plt
with open("data.txt", 'r') as file:
    lines = file.readlines()

data = np.array([list(line.strip()) for line in lines])
data = np.pad(data, ((1,1),(1,1)), 'constant',constant_values=('x','x'))


#-------------------------1-----------------------
start = np.where('^' == data)
state = (int(start[0][0]), int(start[1][0]), '^')

while(True):
    if state[2] == '^':
        if data[state[0]-1,state[1]] == 'x':
            print("done")
            break
        if(data[state[0]-1,state[1]] != '#'):
            next_state = (state[0]-1, state[1], '^')
        else:
            next_state = (state[0], state[1], '>')

    if state[2] == '>':
        if data[state[0],state[1]+1] == 'x':
            print("done")
            break
        if(data[state[0],state[1]+1] != '#'):
            next_state = (state[0], state[1]+1, '>')
        else:
            next_state = (state[0], state[1], 'v')

    if state[2] == '<':
        if data[state[0],state[1]-1] == 'x':
            print("done")
            break
        if(data[state[0],state[1]-1] != '#'):
            next_state = (state[0], state[1]-1, '<')
        else:
            next_state = (state[0], state[1], '^')

    if state[2] == 'v':
        if data[state[0]+1,state[1]] == 'x':
            print("done")
            break
        if(data[state[0]+1,state[1]] != '#'):
            next_state = (state[0]+1, state[1], 'v')
        else:
            next_state = (state[0], state[1], '<')

    state = next_state
    data[state[0]][state[1]] = state[2]


count = np.count_nonzero(data == '>') + np.count_nonzero(data == '<') + np.count_nonzero(data == '^') + np.count_nonzero(data == 'v')

mapping = {'#': 1, 'x': 0, '<': 3, '>': 4, 'v': 5, '^': 6}
numeric_data = np.vectorize(lambda char: mapping.get(char, 2))(data)
plt.imshow(numeric_data)
plt.colorbar()
plt.show()