# Ben Woodfield - Python and Pygame Basics
# The template used in Chapter 1
# Displays a basic black window

# Import the Pygame module into Python
import pygame
from pygame.locals import *
import sys

# Initialise the game
pygame.init()

# Configure window size
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('A Template Program')

# Run the Main/Game loop
while True: 
  for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()

# Update the screen each loop run  
pygame.display.update()
