# Done By: FAdi Masannat
# Help from Mr.David
# PyGame filler code by Mr. David
#Hope you enjoy!


import pygame, sys
from pygame.locals import *
from random import randint
from math import sqrt

# the width/height of our window
WIDTH = 1275
HEIGHT = 650

# Red Bird
red = pygame.image.load('red bird.png')
red = pygame.transform.scale(red, (80, 80))
# Blue Bird
blue = pygame.image.load('blue2.png')
blue = pygame.transform.scale(blue, (80, 80))
# Yellow Bird
yellow = pygame.image.load('yellow bird.png')
yellow = pygame.transform.scale(yellow, (80, 80))
# Black Bird
black = pygame.image.load('black bird.png')
black = pygame.transform.scale(black, (80, 80))
# Mini Pig 1
happy = pygame.image.load('happy_pig.png')
happy = pygame.transform.scale(happy, (80, 80))
# Mini Pig 2
funky = pygame.image.load('funky_pig.png')
funky = pygame.transform.scale(funky, (80, 80))
# Mini Pig 3
chill = pygame.image.load('chill_pig.png')
chill = pygame.transform.scale(chill, (80, 80))
# Guard
guard = pygame.image.load('guard.png')
guard = pygame.transform.scale(guard, (180, 100))
# Guard Positions and speed
guardX = WIDTH - 200
guardY = 150
guardVX = 0
guardVY = 0
# King
king = pygame.image.load('king_pig.png')
king = pygame.transform.scale(king, (120, 120))
# King Positions
kingX = WIDTH - 150
kingY = 0
# Guard Phase 4
injured = pygame.image.load('injured.png')
injured = pygame.transform.scale(injured, (80, 80))
# Guard Phase 3
injuredguard = pygame.image.load('injured guard.png')
injuredguard = pygame.transform.scale(injuredguard, (110, 100))
# Background
background = pygame.image.load('background1.jpg')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
# Branch
branch = pygame.image.load('_rotated branch.png')
branch = pygame.transform.scale(branch, (60, 300))
# Slingshot
slingshot = pygame.image.load('sling.png')
slingshot = pygame.transform.scale(slingshot, (200, 200))
# Hill
hill = pygame.image.load('hill.png')
# Trampoline
trampoline = pygame.image.load('trampoline.png')
# Detector for the guard's death
initiate = False
# Hit Me sign
hit_me = pygame.image.load('hit me.png')
hit_me = pygame.transform.scale(hit_me, (200, 200))
# Hit Me Positions and speeds
hitX = 850
hitY = -300
hitVX = 0
hitVY = 0
# Detector for hitting the sign
trigger = False
# Foreman Pig and positions and speed
foreman = pygame.image.load('foreman.png')
foreman = pygame.transform.scale(foreman, (200, 125))
foremanX = WIDTH
foremanY = HEIGHT - 125
foremanVX = 2
foremanVY = 5
# List of Pigs
pigs = [happy, funky, chill, happy, funky, chill]
# Initial Bird
birds = red
# List of Pig Positions
pigX = [randint(300, WIDTH - 350), randint(300, WIDTH - 350), randint(300, WIDTH - 100), randint(300, WIDTH - 100),
        randint(300, WIDTH - 100), randint(300, WIDTH - 100)]
pigY = [randint(0, 210), randint(0, 210), randint(250, HEIGHT - 50), randint(250, HEIGHT - 100),
        randint(250, HEIGHT - 100), randint(250, HEIGHT - 100)]
# List of Pig speeds
pigVX = [0, 0, 0, 0, 0, 0]
pigVY = [0, 0, 0, 0, 0, 0]
# Initial speed of our Bird
birdVX = 0
birdVY = 0
# Initial mouse values
mouseX = 0
mouseY = 0
# Initial mouse positions
birdX = 53
birdY = 250
# Detector for bouncing on the trampoline
bounce = False
# Detector for the Guard's death
guardbounce = False
# For the rest of the phases of the Guard
guardphase = 0
guard2 = pygame.image.load('hitguard.png')
guard2 = pygame.transform.scale(guard2, (135, 95))
guard3 = pygame.image.load('damagedguard.png')
guard3 = pygame.transform.scale(guard3, (100, 90))
# List of Guard Phases
guardImgs = [guard, guard2, guard3, injuredguard]
# Images of the green texts and numerals
BL0 = pygame.image.load('0.png')
BL0 = pygame.transform.scale(BL0, (600, 600))
BL1 = pygame.image.load('1.png')
BL1 = pygame.transform.scale(BL1, (600, 600))
BL2 = pygame.image.load('2.png')
BL2 = pygame.transform.scale(BL2, (600, 600))
BL3 = pygame.image.load('3.png')
BL3 = pygame.transform.scale(BL3, (600, 600))
BL4 = pygame.image.load('4.png')
BL4 = pygame.transform.scale(BL4, (600, 600))
BL5 = pygame.image.load('5.png')
BL5 = pygame.transform.scale(BL5, (600, 600))
BL6 = pygame.image.load('6.png')
BL6 = pygame.transform.scale(BL6, (600, 600))
BL7 = pygame.image.load('7.png')
BL7 = pygame.transform.scale(BL7, (600, 600))
BL8 = pygame.image.load('8.png')
BL8 = pygame.transform.scale(BL8, (600, 600))
BL9 = pygame.image.load('9.png')
BL9 = pygame.transform.scale(BL9, (600, 600))
BL10 = pygame.image.load('10.png')
BL10 = pygame.transform.scale(BL10, (600, 600))
BL11 = pygame.image.load('11.png')
BL11 = pygame.transform.scale(BL11, (600, 600))
BL12 = pygame.image.load('12.png')
BL12 = pygame.transform.scale(BL12, (600, 600))
BL13 = pygame.image.load('13.png')
BL13 = pygame.transform.scale(BL13, (600, 600))
BL14 = pygame.image.load('14.png')
BL14 = pygame.transform.scale(BL14, (600, 600))
BL15 = pygame.image.load('15.png')
BL15 = pygame.transform.scale(BL15, (600, 600))
BL16 = pygame.image.load('16.png')
BL16 = pygame.transform.scale(BL16, (600, 600))
BL17 = pygame.image.load('17.png')
BL17 = pygame.transform.scale(BL17, (600, 600))
BL18 = pygame.image.load('18.png')
BL18 = pygame.transform.scale(BL18, (600, 600))
BL19 = pygame.image.load('19.png')
BL19 = pygame.transform.scale(BL19, (600, 600))
BL20 = pygame.image.load('20.png')
BL20 = pygame.transform.scale(BL20, (600, 600))
BL21 = pygame.image.load('21.png')
BL21 = pygame.transform.scale(BL21, (600, 600))
BL22 = pygame.image.load('22.png')
BL22 = pygame.transform.scale(BL22, (600, 600))
BL23 = pygame.image.load('23.png')
BL23 = pygame.transform.scale(BL23, (600, 600))
BL24 = pygame.image.load('24.png')
BL24 = pygame.transform.scale(BL24, (600, 600))
BL25 = pygame.image.load('25.png')
BL25 = pygame.transform.scale(BL25, (600, 600))
BL26 = pygame.image.load('26.png')
BL26 = pygame.transform.scale(BL26, (600, 600))
BL27 = pygame.image.load('27.png')
BL27 = pygame.transform.scale(BL27, (600, 600))
BL28 = pygame.image.load('28.png')
BL28 = pygame.transform.scale(BL28, (600, 600))
BL29 = pygame.image.load('29.png')
BL29 = pygame.transform.scale(BL29, (600, 600))
BL30 = pygame.image.load('30.png')
BL30 = pygame.transform.scale(BL30, (600, 600))
BL = pygame.image.load('Birds Left.png')
BL = pygame.transform.scale(BL, (600, 600))
# Images of the red numerals
R0 = pygame.image.load('0R.png')
R0 = pygame.transform.scale(R0, (600, 600))
R1 = pygame.image.load('1R.png')
R1 = pygame.transform.scale(R1, (600, 600))
R2 = pygame.image.load('2R.png')
R2 = pygame.transform.scale(R2, (600, 600))
R3 = pygame.image.load('3R.png')
R3 = pygame.transform.scale(R3, (600, 600))
R4 = pygame.image.load('4R.png')
R4 = pygame.transform.scale(R4, (600, 600))
R5 = pygame.image.load('5R.png')
R5 = pygame.transform.scale(R5, (600, 600))
# The selected position inside the red score list
Red_count = 0
# Our red score list
Score2 = [R5, R4, R3, R2, R1, R0]
# RC is a detector for displaying our text
RC = True
# Detector for winning the game
WIN = False
# Detector for the game loss
endgame = False
# Detector for relaunching the bird
reset = True
# Detector for the death of the King
death = False
# Victory Image
VICTORY = pygame.image.load('VICTORY.png')
# Defeat Image
DEFEAT = pygame.image.load('DEFEAT.png')
# The selected position inside our Birds Left list
Birds_count = 0
# Our Birds Left list
Score1 = [BL30, BL29, BL28, BL27, BL26, BL25, BL24, BL23, BL22, BL21, BL20, BL19, BL18, BL17, BL16, BL15, BL14, BL13,
          BL12, BL11, BL10, BL9, BL8, BL7, BL6, BL5, BL4, BL3, BL2, BL1, BL0]

# Update method ro move blocks
def moveBlocks():
    # Our variables
    global birdX, birdY, birdVX, birdVY, pigX, pigY, pigVX, pigVY, bounce, red, yellow, blue, black, birds, guardX, guardY
    global guardVX, guardVY, guard, guardbounce, guardphase, guard2, guard3, initiate, trigger, hit_me, hitX, hitY, hitVX, hitVY
    global foremanX, foremanVX, foreman, foremanY, Birds_count, endgame, reset, foremanVY, Red_count, RC, WIN, kingX, kingY, death
    # If the game is not over then nothing should move
    if endgame == False and WIN == False:
        birdX += 1 / 15 * birdVX
        birdY += 1 / 15 * birdVY
        guardX += guardVX
        guardY += guardVY
    # If our bird is still moving, we cannot reset it's position
    if birdVX != 0 and birdVY != 0:
        reset = False
    # For changing the size of the foreman
    if -600 <= foremanX <= WIDTH / 3:
        foreman = pygame.transform.scale(foreman, (600, 375))
        foremanY = HEIGHT - 350
    # For changing the size of the foreman
    elif WIDTH/3 <= foremanX <= WIDTH * 2/3:
        foreman = pygame.transform.scale(foreman, (400, 250))
        foremanY = HEIGHT - 225
    # For changing the size of the foreman
    else:
        foreman = pygame.transform.scale(foreman, (200, 125))
    # For changing our red scores
    if 850 <= birdX <= 1000 and 100 <= birdY <= 200 and RC == True and Red_count != 5 and initiate == True:
        Red_count += 1
        RC = False
    # For killing the foreman
    if Red_count == 5:
        trigger = True
    # For moving the foreman and the hit sign
    if initiate == True and endgame == False and trigger == False and WIN == False:
        hitX += hitVX
        hitY += hitVY
        foremanX -= foremanVX
        hitVY = 5
    # For ending the game when the foreman escapes
    if foremanX <= -700:
        endgame = True
    # To end the game when you run out of birds
    if Birds_count == 30 and WIN == False:
        endgame = True
    # Gravity
    if birdVX != 0:
        birdVY += 3
    # for the sign to stop
    if hitY >= 100:
        hitVY = 0
    # For bouncing off the stick
    if 990 <= birdX <= 1050 and -50 <= birdY <= 200:
        birdVX = birdVX * -1
        birdVY = birdVY * -1
    # For collisions between birds and pigs
    for count in range(len(pigs)):
        pigX[count] += pigVX[count]
        pigY[count] += pigVY[count]
        if distance(birdX, birdY, pigX[count], pigY[count]) <= 80:
            pigVX[count] = birdVX * 1 / 15
            pigVY[count] = birdVY * 1 / 15
            birdVX = birdVX * -1 / 2
            birdVY = birdVY * -1 / 2
            pigs[count] = injured
        if pigVX[count] != 0:
            pigVY[count] += 0.3
    # For collisions between birds and the guard
    if distance(birdX, birdY, guardX, guardY) <= 80 and guardbounce == False and bounce == True and guardphase == 3:
        guardVX = birdVX * 1 / 15
        guardVY = birdVY * 1 / 15
        birdVX = birdVX * -1 / 2
        birdVY = birdVY * -1 / 2
        guardbounce = True
        initiate = True

    elif distance(birdX, birdY, guardX, guardY) <= 80 and guardbounce == False and bounce == True and guardphase < 3:
        guardphase += 1
        birdVX = birdVX * -1 / 2
        birdVY = birdVY * -1 / 2
        guardbounce = True
        # For bouncing off the trampoline
    if 1100 <= birdX <= WIDTH and 520 <= birdY <= HEIGHT and bounce == False:
        temp = birdVX
        birdVX = -birdVY / 6
        birdVY = -temp * 2
        bounce = not bounce
    # For colliding with the king
    if distance(birdX, birdY,kingX , kingY) <= 100 and bounce == True and trigger == True:
        death = True
    # For resetting the bird
    if birdX >= WIDTH + 100 or birdX <= -100 or birdY >= HEIGHT + 300 or birdY <= -300:
        birdX = 53
        birdY = 250
        birdVX = 0
        birdVY = 0
        if Birds_count < len(Score1):
            Birds_count += 1
        guardbounce = False
        bounce = False
        if birds == red:
            birds = yellow
        elif birds == yellow:
            birds = blue
        elif birds == blue:
            birds = black
        else:
            birds = red
        reset = True
        RC = True
    # When you die
    if death == True:
        WIN = True
        Birds_count = len(Score1) - 1

# Distance function provided by Mr.David
def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))


# what you want to happen when the mouse is clicked - I provide the
# x and y location of the mouse.
def mouseclicked():
    global mouseX, mouseY
    mouseX = pygame.mouse.get_pos()[0]
    mouseY = pygame.mouse.get_pos()[1]
    # For music
    if endgame == False and WIN == False and reset == True:
       pygame.mixer.music.load('Slingshot.mp3')
       pygame.mixer.music.play()
       pygame.mixer.music.fadeout(1000)



# what you want to happen when the mouse stops being pressed
def mouseReleased():
    global mouseX, mouseY, mouseX2, mouseY2, birdVX, birdVY, birdX, birdY, bounce, reset
    mouseX2 = pygame.mouse.get_pos()[0]
    mouseY2 = pygame.mouse.get_pos()[1]
    if reset == True:
        birdVX = mouseX - mouseX2
        birdVY = mouseY - mouseY2
        birdX = 53
        birdY = 250
    bounce = False

    pygame.mixer.music.stop()


# defines how we want to draw our display
def draw(canvas):
    # set the background white
    canvas.fill((255, 255, 255))
    canvas.blit(background, (0, 0))
    # Draws Everything
    canvas.blit(BL, (-100, -250))
    canvas.blit(Score1[Birds_count], (170, -225))
    if initiate == True and trigger == False:
        canvas.blit(Score2[Red_count], (WIDTH/2 + 50, -200))

    canvas.blit(branch, (1000, -10))
    if death == False:
        canvas.blit(king, (kingX, kingY))
    canvas.blit(guardImgs[guardphase], (guardX, guardY))
    canvas.blit(trampoline, (1075, 500))
    count = 0
    while count < len(pigs):
        canvas.blit(pigs[count], (pigX[count], pigY[count]))
        count += 1
    if trigger == False:
        canvas.blit(foreman, (foremanX, foremanY))
    canvas.blit(birds, (birdX, birdY))
    canvas.blit(slingshot, (25, 250))
    canvas.blit(hill, (-145, 400))
    if trigger == False:
        canvas.blit(hit_me, (hitX, hitY))
    if endgame == True:
        canvas.blit(DEFEAT, (WIDTH/2 - 250, 0))
    if WIN == True:
        canvas.blit(VICTORY, (WIDTH / 2 - 200, HEIGHT / 2 - 150))
    # count2 = 0
    # while count2 < len(birds):

    #  count2 += 1


############## DON'T TOUCH THE BELOW CODE ####################

# always need this to get the pygame functionality going
pygame.init()

# this creates a clock so that we can use time in our game if needed
fps = pygame.time.Clock()

# this creates the window that we will work in, with set width and height
window = pygame.display.set_mode((WIDTH, HEIGHT))

# always give your window a title!
pygame.display.set_caption('Angry Birds')

# loop to keep the game continuously running
while True:

    # update any variables
    moveBlocks()

    # draw our graphics
    draw(window)

    # this cycles through all the events that may happen during the game
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            mouseclicked()
        elif event.type == MOUSEBUTTONUP:
            mouseReleased()

    # update the graphics display
    pygame.display.update()

    # rest for 60 milliseconds
    fps.tick(60)
