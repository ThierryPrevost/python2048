import random
import pygame
import numpy as np
import matplotlib.pyplot as plt

pygame.init()
LARGEUR = 400
HAUTEUR = 500
ecran = pygame.display.set_mode([LARGEUR, HAUTEUR])
pygame.display.set_caption('2048')

timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 24)




colors = {0: (204, 192, 179),
          2: (238, 228, 218),
          4: (237, 224, 200),
          8: (242, 177, 121),
          16: (245, 149, 99),
          32: (246, 124, 95),
          64: (246, 94, 59),
          128: (237, 207, 114),
          256: (237, 204, 97),
          512: (237, 200, 80),
          1024: (237, 197, 63),
          2048: (237, 194, 46),
          'light text': (249, 246, 242),
          'dark text': (119, 110, 101),
          'other': (0, 0, 0),
          'bg': (187, 173, 160)}



game_over = False
spawn_new = True

init_count = 0
direction = ''
somme = 0
file = open('high_score', 'r')
init_high = int(file.readline())
file.close()
high_score = init_high




def init_grid():
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

#grid1 = init_grid()
#print(grid1)



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


#grid2 = add_new(grid1)
#print(grid2)

row = [2, 4, 4, 2]   # >>>[2, 8, 2, 0]

def gauche(row):
    return ([x for x in row if x != 0]+[0]*4)[:4]


def rollin_row(row):
    global somme
    row = gauche(row)
    for i in range(1, 4):
        if row[i] == row[i-1]:
            row[i-1] *= 2
            row[i] = 0
            somme += row[i-1]
    return gauche(row)

#print(rollin_row(row))



def rollin(grid, direction):
    global somme

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



def draw_pieces(grid):
    for i in range(4):
        for j in range(4):
            value = grid[i][j]
            if value > 8:
                value_color = colors['light text']
            else:
                value_color = colors['dark text']
            if value <= 2048:
                color = colors[value]
            else:
                color = colors['other']
            pygame.draw.rect(ecran, color, [j * 95 + 20, i * 95 + 20, 75, 75], 0, 5)
            if value > 0:
                value_len = len(str(value))
                font = pygame.font.Font('freesansbold.ttf', 48 - (5 * value_len))
                value_text = font.render(str(value), True, value_color)
                text_rect = value_text.get_rect(center=(j * 95 + 57, i * 95 + 57))
                ecran.blit(value_text, text_rect)
                pygame.draw.rect(ecran, 'black', [j * 95 + 20, i * 95 + 20, 75, 75], 2, 5)


grid_values = init_grid()
dic = {"u": 0, "d": 0, "l": 0, "r": 0}
run = True

while run:
    timer.tick(fps)
    ecran.fill('red')
    draw_pieces(grid_values)
    if spawn_new or init_count < 2:
        grid_values = add_new(grid_values)
        spawn_new = False
        init_count += 1
    if direction != '':
        grid_values = rollin(grid_values, direction)
        direction = ''
        spawn_new = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            print(dic)
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                direction = 'u'
                dic["u"] += 1
            elif event.key == pygame.K_DOWN:
                direction = 'd'
                dic["d"] += 1
            elif event.key == pygame.K_LEFT:
                direction = 'l'
                dic["l"] += 1
            elif event.key == pygame.K_RIGHT:
                direction = 'r'
                dic["r"] += 1

            elif event.key == pygame.K_ESCAPE:
                print(dic)
                run = False

    if somme > high_score:
        high_score = somme



    if run == False:

        x = ['up', 'down', 'left', 'right']
        y = []


        for valeur in dic.values():
            y.append(valeur)

#sum[
        a = np.array([x, y])

        plt.plot(x, y)
        plt.show()




    pygame.display.flip()
pygame.quit()


