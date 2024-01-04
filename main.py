import pygame
pygame.init()

#variables
screenWidth = 600
screenHeight = 600
board = []
clicked = False
clock = pygame.time.Clock()
pos = []
player = 1
ximg = pygame.image.load('ximg.jpg')
oimg = pygame.image.load('oimg.jpg')

 #screen
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("tic-tac-toe")


def makeGrid ():
    screen.fill((255, 255, 200))
    for x in range(1, 3):
        pygame.draw.line(screen, (50, 50, 50), (0, x * 200), (screenWidth,x * 200), 6) #width
        pygame.draw.line(screen, (50, 50, 50), (x * 200, 0), (x * 200, screenHeight), 6) #height
running = True

for x in range(3):
   row = [0,0,0]
   board.append(row)

def drawMarkers():

    xpos = 0
    ypos = 0

    for column in board:
        for i in column:
            if player == 1:
                screen.blit(ximg, (xpos * 200, ypos * 200 ))
            if player == -1:
                screen.blit(oimg, (xpos * 200, ypos * 200))
            ypos+=1
        xpos+=1





while running:

    makeGrid()
    drawMarkers()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            xval = pos[0]
            yval = pos[1]
            #assigning the array
            if board [xval // 200][yval // 200] == 0:
                board[xval // 200][yval // 200] = player

                print(board)
                player = player*-1




    clock.tick(60)
    pygame.display.update()
pygame.quit()
