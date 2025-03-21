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
GREY = (129, 129, 129)
BALL = (73, 62, 10)

colors = [BLACK, GREEN, BLUE, RED]

def random_color():
    return random.choice(colors)

# init pygame class
pygame.init()

#width and height of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Title of the window
pygame.display.set_caption("CityScroller")

# Loop
done = False

# How fast the screen updates
clock = pygame.time.Clock()



class Building():
    """
    This class will be used to create the building objects.

    It takes:
      x_point - an integer that represents where along the x-axis the building will be drawn
      y_point - an integer that represents where along the y-axis the building will be drawn
      Together the x_point and y_point represent the top, left corner of the building

      width - an integer that represents how wide the building will be in pixels.
            A positive integer draws the building right to left(->).
            A negative integer draws the building left to right (<-).
      height - an integer that represents how tall the building will be in pixels
            A positive integer draws the building up 
            A negative integer draws the building down 
      color - a tuple of three elements which represents the color of the building
            Each element being a number from 0 - 255 that represents how much red, green and blue the color should have.

    It depends on:
        pygame being initialized in the environment.
        It depends on a "screen" global variable that represents the surface where the buildings will be drawn

    """
    def __init__(self, x_point, y_point, width, height, color):
        self.x_point = x_point
        self.y_point = y_point
        self.width = width
        self.height = height
        self.color = color
        
        

    def Draw(self):
        pygame.draw.rect(screen, self.color, [self.x_point, self.y_point, self.width, self.height]) 

        
    def move(self,speed):
        self.x_point -= speed



        
##"""
##        Takes in an integer that represents the speed at which the building is moving
##            A positive integer moves the building to the right ->
##            A negative integer moves the building to the left  <-
##        Moves the building horizontally across the screen by changing the position of the
##        x_point by the speed
##"""



class Scroller(object):
    
    """
    Scroller object will create the group of buildings to fill the screen and scroll

    It takes:
        width - an integer that represents in pixels the width of the scroller
            This should only be a positive integer because a negative integer will draw buildings outside of the screen
        height - an integer that represents in pixels the height scroller
            A negative integer here will draw the buildings upside down.
        base - an integer that represents where along the y-axis to start drawing buildings for this
            A negative integer will draw the buildings off the screen
            A smaller number means the buildings will be drawn higher up on the screen
            A larger number means the buildings will be drawn further down the screen
            To start drawing the buildings on the bottom of the screen this should be the height of the screen
        color - a tuple of three elements which represents the color of the building
              Each element being a number from 0 - 255 that represents how much red, green and blue the color should have.
        speed - An integer that represents how fast the buildings will scroll

    It depends on:
        A Building class being available to create the building obecjts.
        The building objects should have "draw" and "move" methods.
        """

    def __init__(self, width, height, base, color, speed):
        self.width = width
        self.height = height
        self.base = base
        self.color = color
        self.speed = speed
        self.building_list=[]
        self.add_buildings()
        
    def add_building(self, x_location,SCREEN_HEIGHT):
        building_height = random.randint(100,self.height)
        building_width = random.randint(50,175) 
        self.building_list.append( Building(x_location, SCREEN_HEIGHT - building_height, building_width,  building_height , self.color)) 
        

    def add_buildings(self):
        unfilled_width = 0
        while unfilled_width < 800 :
             self.add_building(700-unfilled_width,SCREEN_HEIGHT)
             unfilled_width += self.building_list [-1].width
             
           
        """
        Will call add_building until there the buildings fill up the width of the
        scroller.
        """

    def draw_buildings(self):
        """
        This calls the draw method on each building.
        """
        for b in self.building_list:
            b.Draw()
        

    def move_buildings(self):
        """
        This calls the move method on each building passing in the speed variable
        As the buildings move off the screen a new one is added.
        """
        for m in self.building_list:
            m.move(self.speed)
        for building in self.building_list: 
            if building.x_point + building.width < 0:
                building.x_point = 800

FRONT_SCROLLER_COLOR = (0,0,30)
MIDDLE_SCROLLER_COLOR = (30,30,100)
BACK_SCROLLER_COLOR = (50,50,150)
BACKGROUND_COLOR = (17, 9, 89)

front_scroller = Scroller(SCREEN_WIDTH, 500, SCREEN_HEIGHT, FRONT_SCROLLER_COLOR, 3)
middle_scroller = Scroller(SCREEN_WIDTH, 250, (SCREEN_HEIGHT - 50), MIDDLE_SCROLLER_COLOR, 2)
back_scroller = Scroller(SCREEN_WIDTH, 150, (SCREEN_HEIGHT - 100), BACK_SCROLLER_COLOR, 1)

# -------- Main Program Loop -----------
##
##    x += dx
##    y += dy

while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEMOTION:
              x = pygame.mouse.get_pos() [0]
              y = pygame.mouse.get_pos() [1]
              
    screen.fill(BACKGROUND_COLOR)

    # --- Drawing code
    
    front_scroller.draw_buildings()
    front_scroller.move_buildings()
    middle_scroller.draw_buildings()
    middle_scroller.move_buildings()
    back_scroller.draw_buildings()
    back_scroller.move_buildings()

    # --- Update
    pygame.display.flip()

    # --- 60 fps
    clock.tick(60)

# Close the window and quit.
pygame.quit()

# Needed when using IDLE
exit() 
