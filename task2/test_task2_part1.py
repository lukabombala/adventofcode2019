from . import task2_solution

data = {
    [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]: 3500,
    [1, 0, 0, 0, 99]: 2,
    [2, 3, 0, 3, 99]: 2,
    [2, 4, 4, 5, 99.0]: 2,
    [1, 1, 1, 4, 99, 5, 6, 0, 99]: 30,
}

for k, v in data.items():
    assert task2_solution.fun(k) == v
