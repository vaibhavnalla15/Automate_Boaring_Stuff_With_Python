import random

for i in range(100): # Performs 100 coin flips
    if random.randint(0,1) == 0:
        print("H", end=" ")
    else:
        print("I", end=" ")
print() # print one new line at the end.

print('cats', 'dogs', 'mice', sep=",")