import math


# solution for 1st part
output1 = 0

with open('task1/input1.txt', 'r') as file:
    for line in file:
        line = int(line)
        output1 += math.floor(line/3) - 2

# printing answer
print(output1)

# solution for 2nd part
output2 = 0
with open('task1/input2.txt', 'r') as file:
    for line in file:
        fuel = 0
        mass = int(line)
        while True:
            mass = math.floor(mass/3) - 2
            if mass <= 0:
                break
            fuel += mass
        output2 += fuel

# printing answer
print(output2)
