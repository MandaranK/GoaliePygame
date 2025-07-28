import pygame
import math
import random

def Distance(pos1, pos2):
    return math.sqrt((pos2[0] - pos1[0]) ** 2 + (pos2[1] - pos1[1]) ** 2)

# colours
white = [255, 255, 255]
black = [0, 0, 0]
red =[255, 0, 0]
green = [0, 255, 0]


pygame.init() #initializes the graphics module
windowh = 800
windoww = 800
window = pygame.display.set_mode((windowh, windoww)) #defines window size
pygame.display.set_caption('Game') #names the number
clock = pygame.time.Clock()
font = pygame.font.SysFont("monospace", 25)

#defining variables
Menu = False
background = False
quit = False
ball = 3
Timer = 0
Padl = 100
Padw = 100
paddle_x = 1     #x speed/position
paddle_y = 1     #y speed/position
mousepos = pygame.mouse.get_pos
x_pos = 400
y_pos = 0
score = 0
Mpos = event.pos  #the mouse position is given a variable
right = False
left = False
up = False
down = False
mscreen = pygame.image.load('menu.png')  # menu
bscreen = pygame.image.load('background.png')
def Paddle():
pygame.draw.rect(window, red, mousepos, (Padl, Padw))

if Menu == True:
   window.blit (mscreen, (0, 0))

if background == True:
	window.blit (bscreen, (0, 0))

def gamedraw(): #draws game screen
   global x_pos
   global y_pos
   window.fill(white)
   window.blit(background, (600, 800))
   if not quit:
       window.blit(Paddle(), x_pos, y_pos)

def Start(Num): #clears the screen/restarts
    rad.clear()
    pos.clear()
    vel.clear()
    colour.clear()
    pygame.mouse.set_visible(False)

def randomballs(num)
    for i in range(num):
        rad.append(random.randint(15, 40))
        Randx = random.randint(rad[i], windoww - rad[i])
        Randy = random.randint(rad[i], windowh - rad[i])
        pos.append([Randx, Randy])
        vel.append([random.randint(-5, 5), random.randint(-5, 5)])
        colour.append([random.randint(0, 230), random.randint(0, 230), random.randint(0, 230)])

#event loop
while not quit:
for event in pygame.event.get():
   if event.type == pygame.QUIT:
        quit = True #if quit
   if event.type == pygame.KEYDOWN: #up,down,left,right keys to move paddle
       if event.key == pygame.K_RIGHT:
        right = True
       if event.key == pygame.K_LEFT:
           left = True
       if event.key == pygame.K_UP:
           up = True
       if event.key == pygame.K_DOWN:
           down = True
   if event.type == pygame.KEYUP:
       if event.key == pygame.K_RIGHT:
           right = False
       if event.key == pygame.K_LEFT:
           left = False
       if event.key == pygame.K_UP:
           up = False
       if event.key == pygame.K_DOWN:
           down = False

       if right == True: #if right key is pressed, speed is 2
           x_pos +=2
       if left == True: #if left key is pressed, speed is 2
           x_pos -=2
       if up == True: #if up key is pressed, speed is 2
           y_pos -=2
       if down == True: #if down key is pressed, speed is 2
           y_pos += 2

window.fill((255, 255, 255))

#for collisions with other balls
  c = 0
      while c < (ball):
          if(Distance(Mpos,pos[c]) < playerballrad + rad[c]):
              GameOver = True
            #y = 0
          NextPos1 = (pos[i][0] + vel[i][0],pos[i][1] + vel[i][1])
          NextPos2 = (pos[c][0] + vel[c][0],pos[c][1] + vel[c][1])
          if(Distance(NextPos1,NextPos2) <= rad[i] + rad[c]) and c != i:
              if(rad[i] > rad[c]):
                  vel[i][0] = -vel[i][0]
                  vel[i][1] = -vel[i][1]
                  vel[c][0] = -vel[i][0] + random.randint(-1,1)
                  vel[c][1] = -vel[i][1] + random.randint(-1,1)
            else:
                vel[c][0] = -vel[c][0]
                vel[c][1] = -vel[c][1]
                vel[i][0] = -vel[c][0] + random.randint(-1,1)
                vel[i][1] = -vel[c][1] + random.randint(-1,1)
        c += 1

def leftcollis():
   global x_pos
   global y_pos
   global padw
   while padw + x_pos =< windoww:
       if padw + x_pos =< 0:
           x_pos = 0

def rightcollis():
   global x_pos
   global y_pos
   global padw
   if padw + x_pos >= windoww:
       x_pos = windoww


# timer and add ball
  if not False:
      Timer += 1
      if (math.floor(Timer / 60) >= seconds + 1):
          seconds += 1
      if seconds % 5 == 0:
          for i in range(ball):
              Rand = random.randint(0, 1)
              if vel[i][Rand] > 0:
                  vel[i][Rand] += 1
              else:
                  vel[i][Rand] -= 1

#scoring if a ball flies out of the screen
 if not False:
     pos[i][0] += vel[i][0]
     pos[i][1] += vel[i][1]
 if (pos[i][0] + rad[i] >= windoww or pos[i][0] - rad[i] <= 0):
     score += 1
 if (pos[i][1] + rad[i] >= windowh or pos[i][1] - rad[i] <= 0):
     score+=1

#displays the score on the screen
ScoreText = font.render(str(Score), 1, (0, 0, 0))
BestScoreText = font.render(str(BestScore), 1, (0, 0, 0))
window.blit(ScoreText, (30, 30))
window.blit(BestScoreText, (700, 740))

gamedraw()
Start()
randomballs()
leftcollis()
rightcollis()
#controls timer and adds seconds
if not GameOver:
    Timer += 1
if (math.floor(Timer/60) >= seconds + 1):
    seconds += 1
    if seconds % 5 == 0:
        for i in range(ball):
            Rand = random.randint(0,1)
            if vel[i][Rand] > 0:
                vel[i][Rand] += 1
            else:
                vel[i][Rand] -= 1
     #adds a ball every 10 seconds
    if (seconds % 10 == 0):
        ball += 1
        rad.append(random.randint(15,40))
        Randx = random.randint(rad[i], windoww - rad[i])
        Randy = random.randint(rad[i], windowh - rad[i])
        pos.append([Randx, Randy])
        vel.append([random.randint(-5, 5), random.randint(-5, 5)])
        for Value in vel[-1]:
            if Value == 0:
                Value = 1

        colour.append([random.randint(0,255),random.randint(0,255),random.randint(0,255)])

pygame.display.update() #updates the screen
clock.tick(60)

pygame.quit()
