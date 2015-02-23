"""
 Show how to use a sprite backed by a graphic.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

pygame.init()

	
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

class Rectangle():
	x = ''	
	y = ''
	height = ''
	width = ''
	change_x = ''
	change_y = ''
	
	def move(self):
		self.x += self.change_x
		self.y += self.change_y
		
	def draw(self, screen):
		pygame.draw.rect(screen, GREEN, [self.x, self.y, self.height, self.width])
	

			

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

myObject = Rectangle()
myObject.x = random.randrange(0, 700)
myObject.y = random.randrange(0, 500)
myObject.height = random.randrange(20, 70)
myObject.width = random.randrange(20, 70)
myObject.change_x = random.randrange(-3, 3)
myObject.change_y = random.randrange(-3, 3)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop

    # --- Game logic should go here

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)
    
    myList = []
    
    for i in range(10):
		myList.append(myObject.draw(screen)) + i
	
    
		

	
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()


