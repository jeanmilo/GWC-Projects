"""
 Pygame base template for opening a window

 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Snow")

# Your SnowFlake class

class SnowFlake():
    def __init__ (self, snow_size, x_loc, y_loc, speed):
        self.snow_size = snow_size
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.speed = speed
   
    def fall(self, screen):

        self.y_loc += self.speed
        if self.y_loc >= 500:
            self.y_loc = 10
        pygame.draw.circle(screen,WHITE,[self.x_loc, self.y_loc],self.snow_size)
    
    

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

speed = 3

# Snow List
snow_list = []
##Snow = SnowFlake(30, 350, 10, 3)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    for i in range(10):
        snow_list.append(SnowFlake(random.randint(1,3),random.randint(0,700),0, random.randint(1,5)))

    screen.fill(BLACK)

    # Begin Snow
    
    for flake in snow_list:
        flake.fall(screen)
 
    pygame.display.flip()

    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
