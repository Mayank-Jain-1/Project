"""
pygame Template

  Import 
  Initialize
  Create Window
  Initialize Clock for FPS

  Loop
    Get Events
      if quit
        quit pygame
      apply logic
      update window
      set fps

"""
#import
from operator import truediv
import pygame 
#initialize
pygame.init()

#creatte window display
width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hole in the Screen")

# initialize clock for fps
fps = 30
clock = pygame.time.Clock()

#Main loop
start = True
while start:
  #get events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      start = False
      pygame.quit()
  
  #apply logic
  window.fill((255,255,255))
  pygame.draw.polygon(window,(0,0,0),  ((100,100),(100,200),(200,100)))
  
  #update display
  pygame.display.update()

  #set fps
  clock.tick(fps)

