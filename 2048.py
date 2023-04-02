import numpy as np
import pygame
from pygame.locals import *
import csv
import matplotlib.pyplot as plt

gridsize = 4
screensize = 600
gamedisp = pygame.display.set_mode((screensize, screensize))

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


# grid = init_grid()
# print(grid)

def add_new(grid):
    taille = grid.shape
    taillex = taille[0]
    tailley = taille[1]

    print('grid av:', grid)

    x2 = -1
    y2 = -1

    while x2 == -1 and y2 == -1:

        xtmp = np.random.randint(taillex)
        ytmp = np.random.randint(tailley)

        if grid[xtmp, ytmp] == 0:
            x2 = xtmp
            y2 = ytmp

    if np.random.randint(0, 100) < 80:
        grid[x2, y2] = 2
    else:
        grid[x2, y2] = 4


    #print('x2:', x2)
    #print('y2:', y2)
    #print('grid apres:', grid)
    #print('grid.shape:', grid.shape)

    return grid


# gridnew = add_new(grid)
# print(gridnew)


# row = [2, 4, 4, 2]   # >>>[2, 8, 2, 0]
# row = [8,  0, 16, 0]

def gauche(row):
    return ([x for x in row if x != 0] + [0] * 4)[:4]


# resultat = 0
def rollin_row(row):
    # global resultat
    row = gauche(row)
    for i in range(1, 4):
        if row[i] == row[i - 1]:
            row[i - 1] *= 2
            row[i] = 0
            # resultat += row[i-1]
    return gauche(row)


# print(rollin_row(row))

# grid=np.array([[ 8,  0, 16, 0], [ 4,  0,  0,  0], [ 4,  0,  2,  0], [ 0, 32,  2,  0]])

# grid=[[ 0,  2, 2, 0], [ 0,  4,  4,  0], [ 0,  0,  0,  0], [ 0, 0,  0,  0]]

# print(grid)
def rollin(grid, direction):
    # l (left), r (right), u (up) and d (down).
    # rot90 sens inverse

    gridrotnew = []
    gridnew = []

    if direction == 'l':
        gridrot = grid
        for row in gridrot:
            rowrot = rollin_row(row)
            gridrotnew.append(rowrot)
        gridnew = gridrotnew

    if direction == 'r':
        gridrot = np.rot90(np.rot90(grid))
        for row in gridrot:
            rowrot = rollin_row(row)
            gridrotnew.append(rowrot)
        gridnew = np.rot90((np.rot90(gridrotnew)))

    if direction == 'u':
        gridrot = np.rot90(grid)
        for row in gridrot:
            rowrot = rollin_row(row)
            gridrotnew.append(rowrot)
        gridnew = np.rot90(np.rot90((np.rot90(gridrotnew))))

    if direction == 'd':
        gridrot = np.rot90(np.rot90((np.rot90(grid))))
        # print(grid)
        # print(gridrot)
        for row in gridrot:
            rowrot = rollin_row(row)
            gridrotnew.append(rowrot)
        gridnew = np.rot90(gridrotnew)

    return np.array(gridnew)


# gridnew = rollin(grid, 'l')
# print(gridnew)
# prin(type(gridnew))

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
            pygame.draw.rect(gamedisp, color, [j * 95 + 20, i * 95 + 20, 75, 75], 0, 5)
            if value > 0:
                value_len = len(str(value))
                font = pygame.font.Font('freesansbold.ttf', 48 - (5 * value_len))
                value_text = font.render(str(value), True, value_color)
                text_rect = value_text.get_rect(center=(j * 95 + 57, i * 95 + 57))
                gamedisp.blit(value_text, text_rect)
                pygame.draw.rect(gamedisp, 'black', [j * 95 + 20, i * 95 + 20, 75, 75], 2, 5)
    return


def draw_pieces2(grid):
    decal = 150
    marg = 10
    rectsize = 130
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
            pygame.draw.rect(gamedisp, color, [j * decal + marg, i * decal + marg, rectsize, rectsize], 0, 5)
            if value > 0:
                value_len = len(str(value))
                font = pygame.font.Font('freesansbold.ttf', 48 - (5 * value_len))
                value_text = font.render(str(value), True, value_color)

                pygame.draw.rect(gamedisp, 'black', [j * decal + marg, i * decal + marg, rectsize, rectsize], 2, 5)
    return


def my2048():
    grid = init_grid()

    # print(grid)

    # s = input('--> ')

    pygame.init()
    pygame.display.set_caption("2048")

    run = True
    img = pygame.image.load("pyg.png")
    posX = 50
    vx = 1
    clock = pygame.time.Clock()
    dickey = {"U": 0, "D": 0, "L": 0, "R": 0}
    keylist = []
    filledlist = []
    nolist = []
    maxlist = []

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            gamedisp.fill((220, 220, 220))
            thick = 20
            # pygame.draw.rect(gamedisp, Color("chartreuse4"), (0, 0, screensize, screensize), thick)

            pygame.draw.line(gamedisp, (255, 255, 255), (0, 0), (0, screensize), thick)
            pygame.draw.line(gamedisp, (255, 255, 255), (screensize, 0), (screensize, screensize), thick)
            pygame.draw.line(gamedisp, (255, 255, 255), (0, screensize), (screensize, screensize), thick)
            for line in range(gridsize):
                pygame.draw.line(gamedisp, (255, 255, 255), (0, screensize / gridsize * line),
                                 (screensize, screensize / gridsize * line), thick)
                pygame.draw.line(gamedisp, (255, 255, 255), (screensize / gridsize * line, 0),
                                 (screensize / gridsize * line, screensize), thick)

            # draw_pieces(grid)
            draw_pieces2(grid)

            indexline = 0
            for line in grid:
                indexrow = 0
                marg = 50
                for ele in line:
                    # print(ele)
                    police = pygame.font.SysFont("monospace", 70)
                    if ele != 0:
                        image_texte = police.render(str(ele), 1, (255, 0, 0))
                        gamedisp.blit(image_texte, (
                        screensize / gridsize * indexrow + marg, screensize / gridsize * indexline + marg))
                    indexrow += 1
                indexline += 1
            # print("fin")

            '''
            clock.tick(60)
            # pygame.draw.line(gamedisp, (255, 255, 255), (10, 20), (150, 200), 2)

            pygame.draw.circle(gamedisp, (255, 0, 0), (posX, 300), 30, 2)
            if posX > 770 or posX < 30:
                vx = -vx
            posX = posX + vx
            gamedisp.blit(img, (200, 200))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    print("clic bouton gauche")
                    pos = pygame.mouse.get_pos()
                    print(pos)
                if pygame.mouse.get_pressed() == (0, 0, 1):
                    print("clic bouton droit")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("vous avez appuyé sur la touche espace")
                elif event.key == pygame.K_a:
                    print("vous avez appuyé sur la touche A")
                elif event.key == pygame.K_RETURN:
                    print("vous avez appuyé sur la touche Entrée")
                else:
                    print("vous avez appuyé sur une touche")            

            '''

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    gridnew = rollin(grid, 'u')
                    grid = add_new(gridnew)
                    # print(grid)
                    # print(gridnew)
                    # print("up")
                    dickey["U"] += 1
                    # print(dickey)
                    keylist += "U"
                    # print(grid)
                    # filledlist.append(sum([list(line).count(0) for line in grid]))
                    filledlist.append(sum(np.count_nonzero(line) for line in grid))
                    # print(filledlist)
                    nolist.append(len(nolist) + 1)
                    maxlist.append(max(max(line) for line in grid))

                elif event.key == pygame.K_DOWN:
                    gridnew = rollin(grid, 'd')
                    grid = add_new(gridnew)
                    # print("down")
                    dickey["D"] += 1
                    keylist += "D"
                    filledlist.append(sum(np.count_nonzero(line) for line in list(grid)))
                    nolist.append(len(nolist) + 1)
                    maxlist.append(max(max(line) for line in grid))

                elif event.key == pygame.K_LEFT:
                    gridnew = rollin(grid, 'l')
                    grid = add_new(gridnew)
                    # print("left")
                    dickey["L"] += 1
                    keylist += "L"
                    filledlist.append(sum(np.count_nonzero(line) for line in list(grid)))
                    nolist.append(len(nolist) + 1)
                    maxlist.append(max(max(line) for line in grid))


                elif event.key == pygame.K_RIGHT:
                    gridnew = rollin(grid, 'r')
                    grid = add_new(gridnew)
                    # print("right")
                    dickey["R"] += 1
                    keylist += "R"
                    filledlist.append(sum(np.count_nonzero(line) for line in list(grid)))
                    nolist.append(len(nolist) + 1)
                    maxlist.append(max(max(line) for line in grid))

                elif event.key == pygame.K_ESCAPE:
                    run = False
                    # print("escape")
                elif event.key == pygame.K_SPACE:
                    grid = init_grid()
                    # print("space")
                elif event.key == pygame.K_RETURN:
                    # print("return")
                    run = False
                    # print(dickey)

                    keyvalue = [value for value in dickey.values()]
                    # print (keyvalue)
                    keylabel = [label for label in dickey.keys()]
                    # print(keylabel)

                    if len(nolist) != 0:
                        print(nolist)
                        fig, ax = plt.subplots(2, 2)
                        fig.suptitle('stats des touches appuyées', fontsize=16)

                        # plt.pie(keyvalue, labels=keylabel)
                        # ax[0].title('Nb de touches appuyées')
                        # plt.show()
                        ax[0, 0].pie(keyvalue, labels=keylabel)
                        ax[0, 0].set_title('Nb de touches appuyées')

                        # ax[1].boxplot(keyvalue)
                        ax[0, 1].bar(keylabel, keyvalue)
                        ax[0, 1].set_title('Distribution des freq des touches')

                        ax[1, 0].scatter(filledlist, maxlist)
                        ax[1, 0].set_xlabel('nb cases occupées')
                        ax[1, 0].set_ylabel('max')
                        # ax[1,0].hist(filledlist)
                        ax[1, 0].set_title('max/touches occupées')

                        ax[1, 1].plot(nolist, filledlist, label="nb cases occupées")
                        ax[1, 1].plot(nolist, maxlist, label="max")
                        ax[1, 1].legend()
                        ax[1, 1].set_xlabel('no de tour')
                        ax[1, 1].set_ylabel('valeur')

                        plt.show()

                    '''
                      with open('keyfile.csv', 'w', encoding='UTF8', newline='') as keyfile:
                            writer = csv.writer(keyfile)
                            writer.writerow(keylist)                  

                    keyfile = open('keyfile.txt', 'w')
                    keyfile.write(str(keylist))
                    keyfile.close()

                    with open('keyfile.txt', 'r') as keyfile:
                        keylist = keyfile.read()
                    print(keylist)
                    keylist=list(keylist)

                    keydic = { i : keylist.count(i) for i in keylist }
                    print(keydic)
                    '''


                else:
                    print("veuillez appuyer sur les flèches de direction / espace pour rejouer / entrée pour stats")

        pygame.display.flip()

    pygame.quit()

    # print(filledlist)
    print(nolist)
    print(maxlist)
    # print(dickey)
    # print(keylist)

    return


my2048()

