# main file to load the game 
# for now this file provides structure 
# we will try to make a basic game with no explicit understanding 
# this understanding will be based on a neural network
# here we drive using WASD and there are 3 sensor 
# so input is 3 sensor and the output is AD
# remember it is a look and learn rather than learning itself .....
# so we have to train it hence we play the game for a while and let the neural net train 

# game structure 

import pygame
import time
import random
import trainer
pygame.init()

# add general color functions 
red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)
Height = 800
width = 600
car_h_ratio = 0.45
car_w_ratio = 0.8
x_change = 0
block_start_x = random.randrange(0, width)
block_start_y = - Height
block_speed = random.randint(5, 10)
block_h = 100
block_w = 100
car_width = 136
    
gameDisplay = pygame.display.set_mode((Height, width))

# displaying and restarting the game once it is finished playing .... 
def restart():
    display("you crashed")

def TextObject(text, font):
    TextSurface = font.render(text, True, (255,0,0))
    return TextSurface, TextSurface.get_rect()

def display(text):
    LargeAndBold = pygame.font.Font('freesansbold.ttf', 50)
    Height = 800
    width = 600
    TextSurface, TextRectangle = TextObject(text, LargeAndBold)
    TextRectangle.center = ((width / 2), (Height / 2))
    gameDisplay = pygame.display.set_mode((Height, width))
    gameDisplay.blit(TextSurface, TextRectangle)
    pygame.draw.rect(gameDisplay, (255,0,0),(150,450,100,50))
    pygame.draw.rect(gameDisplay, (0, 255, 0), (550, 450, 100, 50))
    

    pygame.display.update()
    time.sleep(2)
    game_loop()

def button(msg, x, y, w, h, ic, ac, action=None):
    
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()       
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = TextObject(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)


# create a game loop to make life a little easier to edit ...
def game_loop():

    Height = 800
    width = 600
    car_h_ratio = 0.45
    car_w_ratio = 0.8
    x_change = 0
    block_start_x = random.randrange(0, width)
    block_start_y = - Height
    block_speed = random.randint(5, 10)
    block_h = 100
    block_w = 100
    car_width = 136
    
    gameDisplay = pygame.display.set_mode((Height, width))
    pygame.display.set_caption('AI too racey')
    clock = pygame.time.Clock()

    # add images
    backImg = ''
    carImg = 'car.png'
    carImg = pygame.image.load(carImg)

    def blocks(blockx, blocky, blockh, blockw, color):
        pygame.draw.rect(gameDisplay, color, [blockx, blocky, blockw, blockh])

    # def sensor():
    #     return sensor_value # what I don't know is exactly how many I want
        

    def car(x, y):
        gameDisplay.blit(carImg, (x, y))    

    # define size of the car in the display
    x = (Height * car_h_ratio)
    y = (width * car_w_ratio)


    gameExit = False # we keep going till my AI don't crash or I don't crash

    # we start with a loop
    while not gameExit:  
        # get all the events that is happening 
        for event in pygame.event.get():
            if event == pygame.QUIT:
                gameExit = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_QUESTION:
                    gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                    # print("KEYDOWN and LEFT")
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                    # print("KEYDOWN and RIGHT")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

            # print(event) # we see what pygame is receiving 

        x += x_change
        mouse = pygame.mouse.get_pos()  
        # print(x)
        gameDisplay.fill((255, 255, 255))

        # add a few blocks with random speeds and different positions
        blocks(block_start_x, block_start_y, block_h, block_w, (0, 0, 0))
        block_start_y += block_speed
        
        if block_start_y > Height:
            block_start_y -= Height
            block_start_x = random.randrange(0, width)
        

        car(x, y)

        # train() # add the training module here 

        if x < 0 or x > width + car_width:
            restart()

        # interesting part .. crashing the car gives the AI a -1 else the score it receives
        if y < block_start_y + block_h:
            if x > block_start_x and x < block_start_x + block_w or x + car_width < block_start_x + block_w and x + car_width < block_start_x+block_w:
                print("crashed")
        print("Update")
            
                
        pygame.display.update() # update the frame and keep updating the game
        clock.tick(30) # set frame rates .. higher the better 

def quitgame():
    pygame.QUIT


def game_intro():

    Height = 800
    width = 600
    car_h_ratio = 0.45
    car_w_ratio = 0.8
    x_change = 0
    block_start_x = random.randrange(0, width)
    block_start_y = - Height
    block_speed = random.randint(5, 10)
    block_h = 100
    block_w = 100
    car_width = 136
    
    gameDisplay = pygame.display.set_mode((Height, width))
    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill((255,255,255))
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = TextObject("A bit Racey", largeText)
        TextRect.center = ((width/2),(Height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)
        clock = pygame.time.Clock()
        pygame.display.update()
        clock.tick(15)


game_intro()
pygame.quit()
quit()