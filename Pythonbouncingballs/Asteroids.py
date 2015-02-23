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
WHITE    = ( 255, 255, 250)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

exclude_zero_in_change_x_and_y = range(-3, -1) + range(1, 3)

pygame.init()


# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

#define classes
class Ellipse():
	x = ''	
	y = ''
	height, width = '', ''
	change_x = ''
	change_y = ''

	def move(self):
		self.x += self.change_x
		self.y += self.change_y

	def draw(self, screen):
		pygame.draw.ellipse(screen, WHITE, [self.x, self.y, self.height, self.width], 1)


pygame.display.set_caption("Bouncing Meteors")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

Asteroid = Ellipse()

Asteroid_List = []

for i in range(10):
        Asteroid.x = random.randrange(70, 630)
        Asteroid.y = random.randrange(300, 430)
        Asteroid.height = 70
        Asteroid.width = 70
        Asteroid.change_x = random.choice(exclude_zero_in_change_x_and_y)
        Asteroid.change_y = random.choice(exclude_zero_in_change_x_and_y)
	Asteroid_List.append([Asteroid])

Asteroid.draw(screen)
Asteroid.move

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
    
    for i in range(len(Asteroid_List)):
		Asteroid.draw(screen)
		Asteroid.move()
    
		if Asteroid.y > 430 or Asteroid.y < 0:
			Asteroid.change_y = Asteroid.change_y * -1
		if Asteroid.x > 630 or Asteroid.x < 0:
			Asteroid.change_x = Asteroid.change_x * -1
  

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
