# solution for 1st part

with open("input1.txt", "r") as file:
    _str = file.readlines()

program = _str[0].strip().split(',')
program = [int(elem) for elem in program]

program[1] = 12
program[2] = 2


def fun(prog):
    ind = 0
    while prog[ind] != 99:
        if prog[ind] == 1:
            prog[prog[ind + 3]] = prog[prog[ind + 1]] + prog[prog[ind + 2]]
        elif prog[ind] == 2:
            prog[prog[ind + 3]] = prog[prog[ind + 1]] * prog[prog[ind + 2]]
        ind += 4
    return prog


print(fun(program)[0])
