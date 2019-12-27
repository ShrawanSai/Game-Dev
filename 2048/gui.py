import pygame
from l2048 import *
pygame.init()


display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('2048')

t0 = pygame.image.load('0.png')
t2 = pygame.image.load('2.png')
t4 = pygame.image.load('4.png')
t8 = pygame.image.load('8.png')
t16 = pygame.image.load('16.png')
t32 = pygame.image.load('32.png')
t64= pygame.image.load('64.png')
t128 = pygame.image.load('128.png')
t256 = pygame.image.load('256.png')
t512 = pygame.image.load('512.png')
t1024 = pygame.image.load('1024.png')
t2048 = pygame.image.load('2048.png')


block_dict={0:t0,2:t2,4:t4,8:t8,16:t16,32:t32,64:t64,128:t128,256:t256,512:t512,1024:t1024,2048:t2048}

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()

positions={1:(125,25),2:(275,25),3:(425,25),4:(575,25),
            5:(125,175),6:(275,175),7:(425,175),8:(575,175),
            9:(125,325),10:(275,325),11:(425,325),12:(575,325),
            13:(125,475),14:(275,475),15:(425,475),16:(575,475)}


kep_p={(0,0):1,
(0,1):2,
(0,2):3,
(0,3):4,
(1,0):5,
(1,1):6,
(1,2):7,
(1,3):8,
(2,0):9,
(2,1):10,
(2,2):11,
(2,3):12,
(3,0):13,
(3,1):14,
(3,2):15,
(3,3):16}

def tile(tilep,pos):
    gameDisplay.blit(tilep, positions[pos])

def game_loop():

    gameExit=False

    board=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    board=initial_setup(board)
    print(board)
    print('________________________________________________________')
    while not gameExit:
        move='a'
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type==event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move='u'
                elif event.key == pygame.K_DOWN:
                    move='d'
                elif event.key == pygame.K_LEFT:
                    move='l'
                elif event.key == pygame.K_RIGHT:
                    move='r'
            elif event.type==event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    move='a'
                elif event.key == pygame.K_DOWN:
                    move='a'
                elif event.key == pygame.K_LEFT:
                    move='a'
                elif event.key == pygame.K_RIGHT:
                    move='a'
            prev=board
            #move=input('Enter l,r,u,d-  ')
            if move=='l':
                board=key_left(board)
            elif move=='r':
                board=key_right(board)
            elif move=='u':
                board=key_up(board)
            elif move=='d':
                board=key_down(board)
            #print(board)
            #print('###########################3')
           
            if move!='a':
                board=genrate_block(board)
                
            #print(board)
            #print('###########################3')
            #print('###########################3')
            #print('###########################3')
        gameDisplay.fill(white)

        for row in range(len(board)):
            for col in range(len(board[0])):
                val=kep_p[(row,col)]
                box_val=board[row][col]
                t_value=block_dict[box_val]
                tile(t_value,val)
                
    

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()


