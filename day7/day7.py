import numpy as np
from itertools import product
with open("data.txt", 'r') as file:
    txt = file.read().splitlines()

print(txt)
#--------------------1+2-----------------------
def operations(op, n):
    return list(product(op, repeat=n))

def custom_eval(ops, nums):
    result = numbers[0]
    for i in range(len(ops)):
        if ops[i] == '+':
            result += numbers[i + 1]
        elif ops[i] == '*':
            result *= numbers[i + 1]
        elif ops[i] == '||':
            result = int(str(result) + str(numbers[i+1]))
    return result

count = 0
for line in txt:
    left, right = line.split(":")
    left = left.strip().split(" ")
    right = right.strip().split(" ")
    print(right)

    operator_combos = operations(['+', '*', '||'],len(right)-1)
    for ops in operator_combos:
        """
        geht leidern icht, weil punkt vor strich ignoriert werden soll :( )
        expression =  "".join( num + op for num, op in zip(right, ops)) + right[-1] g
        value = eval(expression)
        """
        numbers = list(map(int, right))
        result = custom_eval(ops, numbers)

        #print(f"taget = {left[0]}  und ergebnis = {result} \n")
        if(result == int(left[0])):
            count += result
            break
       
print(count)


