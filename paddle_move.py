import pygame 
import random
import math 
# -- Global Constants  

# -- Colours  
BLACK = (0,0,0)  
WHITE = (255,255,255)  
BLUE = (50,50,255)  
YELLOW = (255,255,0)  

# -- Initialise PyGame
pygame.init()  

# -- Blank Screen  
size = (640,480)  
screen = pygame.display.set_mode(size)  
# -- Title of new window/screen  
pygame.display.set_caption("My Window")  
# -- Exit game flag set to false  
done = False 
# -- Manages how fast screen refreshes  
clock = pygame.time.Clock() 

## rectangle x and y coordinates
x_coord = 50
y_coord = 50

## rectangle x and y speed
x_speed = 0
y_speed = 0

### -- Game Loop  
while not done: 

  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          done = True
      # User pressed down on a key
      elif event.type == pygame.KEYDOWN:
          # Figure out if it was an arrow key. If so
          # adjust speed.
          if event.key == pygame.K_LEFT:
              x_speed = -3
          elif event.key == pygame.K_RIGHT:
              x_speed = 3
          elif event.key == pygame.K_UP:
              y_speed = -3
          elif event.key == pygame.K_DOWN:
              y_speed = 3
      ## end if
  
      # User let up on a key
      elif event.type == pygame.KEYUP:
          # If it is an arrow key, reset vector back to zero
          if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
              x_speed = 0
          elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
              y_speed = 0
          ## end if
      ## end if
  ## end For

  # Move the object according to the speed vector.
  x_coord += x_speed
  y_coord += y_speed
 

  # - Screen background is BLACK  
  screen.fill (BLACK)  
  
  # -- Draw rectangle
  pygame.draw.rect(screen, BLUE, (x_coord,y_coord,50,50)) 

  # -- flip display to reveal new position of objects  
  pygame.display.flip()
  # - The clock ticks over  
  clock.tick(60)  
#End While - End of game loop  
pygame.quit()
