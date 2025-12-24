#initialize pygame and screen dimensions
import pygame
pygame.init()
SCREEN_WIDTH,SCREEN_HEIGHT=500,500
#iniyialize display surface and set title
display_surface=pygame.display.setmodel((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.disaplay.set_caption( ' adding image to the backgrounf image')
#load and scale images directly
backgrounf_image=pygame.transform.scale(
    pygame.image.load('backgrounf.png').convert(),
    (SCREEN_WIDTH,SCREEN_HEIGHT))
penguin_image=pygame.transform.scale(
    pygame.image.load('hello penguin.png').convert_alpha(),(200,200))
penguin_rect=penguin_image.get_rect(center=(SCREEN_WIDTH//2,
                                            SCREEN_HEIGHT//2-30))
#INITIALISE FONT,RENDER TEXT,AND SET POSITION
text=pygame.font.Font(None,36).render('HellO world',True,
                                      pygame.Color('black'))
text_rect=text.get_rect(center=(SCREEN_WIDTH//2,SCREEN_HEIGHT//2+110))

