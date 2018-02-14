import pygame
from random import randint

pygame.init()

display_width = 800
display_height = 500

black = (0,0,0)
red = (255,0,0)
background = (223, 230, 233)

circle_x = 100
circle_y = 100

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()

def things(thingX, thingY, thingW, thingH, color):
    pygame.draw.rect(gameDisplay, color, [thingX, thingY, thingW, thingH])

def Ball (circle_x, circle_y):
        pygame.draw.rect(gameDisplay, (0, 184, 148), [circle_x, circle_y, 10, 10])

score_1 = 0
score_2 = 0

def font (score_1, score_2):
        pygame.font.init()
        myfont = pygame.font.SysFont('System', 400)
        textsurface = myfont.render(str(score_1), True, (164, 176, 190))
        textsurface2 = myfont.render(str(score_2), True, (164, 176, 190))
        gameDisplay.blit(textsurface,(display_width - display_width/3, display_height / 2 - 120))
        gameDisplay.blit(textsurface2,  (display_width/6, display_height / 2 - 120))
        
def game_loop():

    x = (display_width * 0.45)
    y = (display_height * 0.8)
    
    thing_startx = 20
    thing_starty = display_height/2 - 50
    thing_speed = 7
    thing_width = 10
    thing_height = 100
    
    # Game speed
    speed_x = 5
    speed_y = 2
    
    circle_x = display_width/2 - 10
    circle_y = display_height/2 - 10

    ai_y = display_height/2 - 50
    up = 0
    
    direction = [1,1]

    check = False

    y_pos = 200

    gameExit = False
    
    global score_1
    global score_2

    while not gameExit:

        y_pos = pygame.mouse.get_pos()[1]
    
        if y_pos <= 50 :
            y_pos = 50
        elif y_pos >= display_height - 50 :
            y_pos = display_height - 50
        
        circle_x += direction[0] * speed_x
        circle_y += direction[1] * speed_y

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                
            if event.type == pygame.KEYDOWN :
                
                if event.key == ord('a'):
                    up = -5
                    
                elif event.key == ord('z'):
                    up = 5
            if event.type == pygame.KEYUP :
                
                if event.key == ord('a'):
                    up = 0
                    
                elif event.key == ord('z'):
                    up = 0

        ai_y += up

        gameDisplay.fill(background)
        
        # Player
        things(display_width - 2*thing_startx + 10, y_pos - 50, thing_width, thing_height, (9, 132, 227))

        # AI Boundaries

        if ai_y >= display_height - 100 :
            ai_y = display_height - 100
        elif ai_y <= 0 :
            ai_y = 0
        
        things(thing_startx, ai_y, thing_width, thing_height, (214, 48, 49))


        pygame.draw.rect(gameDisplay, (0, 184, 148), [display_width/2, 0, 2, display_height])

        # Player 1 Logic

        if circle_x == display_width - 2*thing_startx  and circle_y <= y_pos + 50 and circle_y > y_pos - 50 :
            direction[0] = -1

            if y_pos < circle_y :
                direction[1] = 1
                
            elif y_pos >= circle_y :
                direction[1] = -1

            check = False

        if circle_y == 0 :
            direction[0] = -1
            direction[1] = 1
            
        elif circle_y == display_height - 10 :
            direction[0] = -1
            direction[1] = -1

        # Player 2 Logic 

        if circle_x == 2*thing_startx - 10 and circle_y <= ai_y + 100 and circle_y > ai_y - 10 :
                
            direction[0] = 1

            check = True
                
        if circle_y == 0 and check :
            direction[0] = 1
            direction[1] = 1
            
        elif circle_y == display_height - 10 and check :
            direction[0] = 1
            direction[1] = -1

        if circle_x == 0 :
            score_1 += 1
            game_loop()

        elif circle_x == display_width:
            score_2 += 1
            game_loop()

        font (score_1, score_2)
            
        Ball (circle_x, circle_y)
                
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
