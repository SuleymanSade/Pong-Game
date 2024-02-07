import pygame
import random

pygame.init()

global leftRect, rightRect, direction, ySpeed, rightRectScore, leftRectScore, circleX, circleY, startButton
clock =pygame.time.Clock()
FPS =60

speedChangeRate = 0.075 # per sec
rectangleSpeed = 900/FPS
ySpeed = 180/FPS

leftRectScore = 0
rightRectScore = 0

# Set up the screen
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# setting Y of right and left blocks
rightY = 0
leftY =0

font = pygame.font.SysFont('monospace', 15)

# Colors
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

running = True

pygame.display.set_caption("2 Player Game")

def reset():
    global direction, ySpeed, circleY, circleX, speed
    
    # Random starting direction (l = left, r = right)
    direction = 'l' if random.randint(0,1)==0 else 'r'

    # Random starting up or down
    ySpeed *= 1 if random.randint(0,1)==0 else -1
    
    speed = 180/FPS


    # Initial circle position
    circleX = screen_width/2
    circleY = screen_height/2

def key_handler():
    global leftY, rightY
    key = pygame.key.get_pressed()
    if leftY>0:
        if key[pygame.K_w]:
            leftY-=rectangleSpeed
    if leftY+120<screen_height:
        if key[pygame.K_s]:
            leftY+=rectangleSpeed
    if rightY+120<screen_height:
        if key[pygame.K_DOWN]:
            rightY+=rectangleSpeed
    if rightY>0:
        if key[pygame.K_UP]:
            rightY-=rectangleSpeed
        
def collision_checker():
    global leftRect, rightRect, direction, ySpeed
    collideLeftRect = leftRect.collidepoint((circleX,circleY))
    collideRightRect = rightRect.collidepoint((circleX,circleY))
    
    if collideLeftRect:
        direction = 'r'
    if collideRightRect:
        direction = 'l'
        
    if circleY < 0 or circleY> screen_height:
        ySpeed *=-1

def win_checker():
    global rightRectScore, leftRectScore
    if circleX < 0:
        rightRectScore+=1
        reset()
    elif circleX > screen_width:
        leftRectScore+=1
        reset()
    
reset()
while running:
    pygame.display.update()
    # pygame_widgets.update(pygame.event.get())
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    key_handler()
    screen.fill((0,0,0))
    
    leftRect = pygame.draw.rect(screen, green, (20, leftY, 20, 120))
    rightRect = pygame.draw.rect(screen, red, (screen_width-40, rightY, 20, 120))
        
    circle = pygame.draw.circle(screen, white, (circleX,circleY), 20)
    
    scoreLabel = font.render(str(leftRectScore)+':'+str(rightRectScore), 1, blue)
    screen.blit(scoreLabel, (screen_width/2,0))

    collision_checker()
    
    if direction == 'l':
        circleX -= speed
    if direction == 'r':
        circleX += speed
    circleY+=ySpeed
    
    ySpeed+= speedChangeRate/FPS
    speed+= speedChangeRate/FPS
    rectangleSpeed+= speedChangeRate/FPS
    
    win_checker()
    
    clock.tick(FPS)



# Quit Pygame
pygame.quit()