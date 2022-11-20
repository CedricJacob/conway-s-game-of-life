import pygame, copy, random
from copy import deepcopy

pygame.init()

DISPLAY = pygame.display.set_mode((800, 800))
fps = pygame.time.Clock()
run = True
the_f = 20

worldrep = [[0 for i in range(40)] for x in range(40)]
world = [[0 for i in range(40)] for x in range(40)]
# world = [[random.randint(0, 1) for i in range(40)] for j in range(40)]

pause = False
write = False

def grid():     
    for i in range(40):
        for j in range(40):
            pygame.draw.line(DISPLAY, "dimgray", (0, i * 20), (800, i * 20))
            pygame.draw.line(DISPLAY, "dimgray", (j * 20, 0), ( j * 20, 800))
            

def checksc(cf, x, y):
    c = 0
    for i in range(x - 1, x + 2): # default should be y first before x
        for j in range(y - 1, y + 2):
            if cf[i][j]:
                c += 1
    
    if cf[x][y]:
        c -= 1 # subtracting bc it only count the nieghbors not including itself
        if c == 2 or c == 3: 
            return 1
        #else: if not c == 2 or c == 3:   
        return 0
    else:
        if c == 3:
            return 1
        #else: if not c == 3:
        return 0
    
def real_time():
    global world
    if not pause:
        for i in range(len(world) - 1):
            for j in range(len(world) - 1):
                worldrep[i][j] = checksc(world, i, j)
        
        world = deepcopy(worldrep)
        
    for i in range(len(world)):
        for j in range(len(world)):
            if world[i][j] == 1:
                pygame.draw.rect(DISPLAY, 'darkgreen', (i * 20, j * 20, 20, 20))

def test_draw():
    if pause and write:
        mousex, mousey = pygame.mouse.get_pos()
        for i in range(len(world)):
            for j in range(len(world)):
                test_rect = pygame.Rect(j * 20, i * 20, 20, 20)
                if abs(test_rect.center[0] - mousex) <= 10 and abs(test_rect.center[1] - mousey) <= 10:
                    world[j][i] = 1

while run:
    fps.tick(the_f)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if pygame.K_SPACE:
                if not pause:
                    the_f = 100
                    pause = True
                else:
                    the_f = 20
                    pause = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                    write = True
        if  event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                write = False
    
    key = pygame.key.get_pressed()
    
    DISPLAY.fill("black")
    
    test_draw()
    
    real_time()
    
    grid()
    
    pygame.display.update()
    
pygame.quit()