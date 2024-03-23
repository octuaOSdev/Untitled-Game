#what are you doing here?
#your are NOT supposed to be here
#get out of here
# Importing pygame module 
import pygame 
from pygame.locals import *
  
# initiate pygame and give permission 
# to use pygame's functionality. 
pygame.init() 
  
# create the display surface object 
# of specific dimension. 
window = pygame.display.set_mode((600, 600)) 
  
# Add caption in the window 
pygame.display.set_caption('UNtitled Game') 
  
# Initializing the clock 
# Clocks are used to track and 
# control the frame-rate of a game 
clock = pygame.time.Clock() 
  
# Add player sprite 
image = pygame.image.load(r'Soul.png') 
  
  
# Store the initial 
# coordinates of the player in 
# two variables i.e. x and y. 
x = 100
y = 100
  
# Create a variable to store the 
# velocity of player's movement 
velocity = 12
  
# Creating an Infinite loop 
run = True
while run: 
  
    # Set the frame rates to 60 fps 
    clock.tick(60) 
  
    # Filling the background with 
    # white color 
    window.fill((255, 255, 255)) 
  
    # Display the player sprite at x 
    # and y coordinates 
    window.blit(image, (x, y)) 
  
    # iterate over the list of Event objects 
    # that was returned by pygame.event.get() method. 
    for event in pygame.event.get(): 
  
        # Closing the window and program if the 
        # type of the event is QUIT 
        if event.type == pygame.QUIT: 
            run = False
            pygame.quit() 
            quit() 
  
    # Storing the key pressed in a 
    # new variable using key.get_pressed() 
    # method 
    key_pressed_is = pygame.key.get_pressed() 
  
    # Changing the coordinates 
    # of the player 
    if key_pressed_is[K_LEFT]: 
        x -= 8
    if key_pressed_is[K_RIGHT]: 
        x += 8
    if key_pressed_is[K_UP]: 
        y -= 8
    if key_pressed_is[K_DOWN]: 
        y += 8
  
    # Draws the surface object to the screen. 
    pygame.display.update() 