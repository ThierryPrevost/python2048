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


grid3 = np.array([[8, 0, 16, 0], [4, 0, 0, 0], [4, 0, 2, 0], [0, 32, 2, 0]])
print(grid3)

somme = 0

def rollin2(grid, direction):
    fus = [[False for _ in range(4)] for _ in range(4)]
    if direction == 'u':
        for i in range(4):
            for j in range(4):
                pas = 0
                if i > 0:
                    for k in range(i):
                        if grid[k][j] == 0:
                            pas += 1
                    if pas > 0:
                        grid[i - pas][j] = grid[i][j]
                        grid[i][j] = 0
                    if grid[i - pas - 1][j] == grid[i - pas][j] and not fus[i - pas][j] \
                            and not fus[i - pas - 1][j]:
                        grid[i - pas - 1][j] *= 2
                        somme += grid[i - pas - 1][j]
                        grid[i - pas][j] = 0
                        fus[i - pas - 1][j] = True

    elif direction == 'd':
        for i in range(3):
            for j in range(4):
                pas = 0
                for k in range(i + 1):
                    if grid[3 - k][j] == 0:
                        pas += 1
                if pas > 0:
                    grid[2 - i + pas][j] = grid[2 - i][j]
                    grid[2 - i][j] = 0
                if 3 - i + pas <= 3:
                    if grid[2 - i + pas][j] == grid[3 - i + pas][j] and not fus[3 - i + pas][j] \
                            and not fus[2 - i + pas][j]:
                        grid[3 - i + pas][j] *= 2
                        somme += grid[3 - i + pas][j]
                        grid[2 - i + pas][j] = 0
                        fus[3 - i + pas][j] = True

    elif direction == 'l':
        for i in range(4):
            for j in range(4):
                pas = 0
                for k in range(j):
                    if grid[i][k] == 0:
                        pas += 1
                if pas > 0:
                    grid[i][j - pas] = grid[i][j]
                    grid[i][j] = 0
                if grid[i][j - pas] == grid[i][j - pas - 1] and not fus[i][j - pas - 1] \
                        and not fus[i][j - pas]:
                    grid[i][j - pas - 1] *= 2
                    somme += grid[i][j - pas - 1]
                    grid[i][j - pas] = 0
                    fus[i][j - pas - 1] = True

    elif direction == 'r':
        for i in range(4):
            for j in range(4):
                pas = 0
                for k in range(j):
                    if grid[i][3 - k] == 0:
                        pas += 1
                if pas > 0:
                    grid[i][3 - j + pas] = grid[i][3 - j]
                    grid[i][3 - j] = 0
                if 4 - j + pas <= 3:
                    if grid[i][4 - j + pas] == grid[i][3 - j + pas] and not fus[i][4 - j + pas] \
                            and not fus[i][3 - j + pas]:
                        grid[i][4 - j + pas] *= 2
                        somme += grid[i][4 - j + pas]
                        grid[i][3 - j + pas] = 0
                        fus[i][4 - j + pas] = True
    return grid


direction = 'r'
print(rollin2(grid3, direction))


