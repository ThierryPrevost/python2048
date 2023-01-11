import numpy as np


def init_grid():
    m = np.zeros((4, 4), dtype=int)

    x1 = np.random.randint(4)
    y1 = np.random.randint(4)

    m[x1, y1] = 2

    x2 = x1
    while x2 == x1:
        x2 = np.random.randint(4)

    y2 = y1
    while y2 == y1:
        y2 = np.random.randint(4)

    m[x2, y2] = 2

    return m


def init_grid2():
    grid = np.zeros((4, 4), dtype=int)

    x1 = np.random.randint(4)
    y1 = np.random.randint(4)

    grid[x1, y1] = 2

    x2 = x1
    while x2 == x1:
        x2 = np.random.randint(4)

    y2 = y1
    while y2 == y1:
        y2 = np.random.randint(4)

    grid[x2, y2] = 2
    return grid


grid1 = init_grid2()
print(grid1)


def add_new2(grid):
    taille = grid.shape
    tailley = taille[0]
    taillex = taille[1]

    x2 = 0
    y2 = 0
    for y1 in range(tailley):

        for x1 in range(taillex):

            while grid[x1, y1] == 0 and y2 == 0:
                y2 = np.random.randint(tailley)

            while grid[x1, y1] == 0 and x2 == 0:
                x2 = np.random.randint(taillex)

    if np.random.randint(0, 100) < 80:
        grid[x2, y2] = 2
    else:
        grid[x2, y2] = 4

    return grid


grid2 = add_new2(grid1)
print(grid2)


def add_new(grid):
    taille = grid.shape
    tailley = taille[0]
    taillex = taille[1]

    x2 = 0
    y2 = 0
    for y1 in range(tailley):

        for x1 in range(taillex):

            while grid[x1, y1] == 0 and y2 == 0:
                y2 = np.random.randint(tailley)

            while grid[x1, y1] == 0 and x2 == 0:
                x2 = np.random.randint(taillex)

    if np.random.randint(0, 100) < 80:
        grid[x2, y2] = 2
    else:
        grid[x2, y2] = 4

    return grid


row = [2, 4, 4, 2]  # >>>[2, 8, 2, 0]


def gauche(row):
    return ([x for x in row if x != 0] + [0] * 4)[:4]

def rollin_row(row):

    row = gauche(row)
    for i in range(1, 4):
        if row[i] == row[i - 1]:
            row[i - 1] *= 2
            row[i] = 0

    return gauche(row)


print(rollin_row(row))

