import pygame
import random
import time
pygame.init()


display_width = 800
display_height = 600
move_space=200


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Flappy Bird')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False
birdImg = pygame.image.load('bird.png')


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(3)
    gameExit = False
    game_loop()
    
    

def crash():
    message_display('LOL you died')
def away():
    message_display('OUT')


def pillar(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])




def bird(x,y):
    gameDisplay.blit(birdImg, (x,y))


def game_loop():


    x =  (display_width * 0.2)
    y = (display_height * 0.6)
    y_change = 5
    bird_speed = 0
    bird_width = 64
    bird_s=90

    thing_starty =0
    thing_startx = 700
    thing_speed = -7
    thing_width = 200
    thing_height = random.randrange(0,  0.6*display_height)

    lower_py=thing_height+move_space
    lower_px=thing_startx
    lower_width=thing_width
    lower_height=display_height-lower_py


    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            ############################
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    y_change = -10   
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    y_change = 5 
            ######################
        ##
        y += y_change
        #y_change=0
    ##         

        gameDisplay.fill(white)

        pillar(thing_startx, thing_starty, thing_width, thing_height, black)
        pillar(lower_px, lower_py, lower_width, lower_height, black)
        thing_startx += thing_speed
        lower_px+=thing_speed

        bird(x,y)
        #print(y)
        if y > display_height - bird_width or y < 0.0:
            #print(111)
            away()

        if thing_startx + thing_width < 0:
            thing_starty =0
            thing_startx = 700
            #thing_speed = -7
            #thing_width = 300
            thing_height = random.randrange(0, 0.6*display_height)
            lower_py=thing_height+move_space
            lower_px=thing_startx
            #lower_width=300
            lower_height=display_height-lower_py
            
        if x+ bird_s > thing_startx and x<thing_startx+thing_width:
            #print('x crossover')

            if y< thing_starty+thing_height or y+bird_width>lower_py:
                #print('y crossover')
                crash()
                gameExit=True                    
        pygame.display.update()
        clock.tick(40)

game_loop()
pygame.quit()
quit()
