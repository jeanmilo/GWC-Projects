"""
 Pygame base template for opening a window
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

aaa = 0
bbb = 0
ccc = 0
dd = 5

if ccc == 255 or aaa == 255 or bbb == 255:
    dd = -dd

BLACK = (0, 0, 0)
NICE = (93, 131, 93)
OKOK = (aaa + dd , bbb + dd, ccc + dd)

pygame.init()


SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("i really dont like python pls save me")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# WRITE YOUR CODE HERE
x = y = 0

dx = 1
dy = 3


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    x += dx
    y += dy


    # --- Game logic should go here
    if x + dx < 0 or x + dx > SCREEN_WIDTH - 30:
        dx = -dx
    if y + dy < 0 or y + dy > SCREEN_HEIGHT - 30:
        dy = -dy 

##    if x == SCREEN_WIDTH - 30:
##        x -= dx
##
##    if y == SCREEN_HEIGHT - 30:
##        y -= 3
##
##    if y == 30:
##        y += 2
##
##    if x == 30:
##        x += 2

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here

    pygame.draw.circle (screen, NICE, (x, y), random.randint(40,60), 0)


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
