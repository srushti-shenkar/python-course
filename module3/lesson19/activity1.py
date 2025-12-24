#import necesaary libraries
import pygame
#initialize required modules
pygame.init()
#setup window gemometry
screen=pygame.display.set_mode((400,500))
#create a loop till the game is quit by the user
done=False
while not done:
    #clear the event queue
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    #make the chnages visible
    pygame.display.flip()