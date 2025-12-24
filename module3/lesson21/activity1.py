import pygame
import random
#initialize pygame
pygame.init()
#custom event ID's for color change events
SPRITE_COLOR_CHANGE_EVENT=pygame.USEREVENT+1
BACKGROUND_COLOR_CHANGE_EVENT=pygame.USEREVENT+2
#define basic colors using pygame.colors
#background colors
RED=pygame.Colors('red')
ORANGE=pygame.Colors('orange')
GREEN=pygame.Colors('green')
#sprite colors
YELLOW=pygame.Colors('yellow')
MAGENTA=pygame.Colors('magenta')
PURPLE=pygame.Colors('orange')
WHITE=pygame.Colors('white')
#sprite class reprensenting the moving object
class Sprite(pygame.sprite.Sprite):
    #constructor method
    def __init__(self,color,height,width):
        #call to the parent class(Sprite constructor)
        super().__init__()
        #create the sprites surface with dimension and color
        self.image=pygame.Surface([width,height])
        self.image.fill(color)
        #get the sprite's rect defining its position and size
        self.rect=self.image.get_rect()
        #set initial velocity with random directions
        self.velocity=[random.choice([-1,1]),random.choice([-1,1])]
        #method to update the sprite's position
        def update(self):
            #move the sprite to its velocity
            self.rect.move_ip(self.velocity)
            #flag to track if the sprite hits a boundary
            boundary_hit=False
            #check the collision with left or right boundaries and reverse directions
            if self.rect.left<=0 or self.rect.right>=500:
                self.velocity[0]=-self.velocity[0]
                boundary_hit=True
                #check for the collisipns with top or bottom boundaries and reverse directions
                if self.rect.top<=0 or self.rect.bottom>=400:
                    self.velocity[1]=-self.velocity[1]
                    boundary_hit=True
                    #if a boundary was hit,post event to change colors
                    if boundary_hit:
                        pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
                        pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))
                        #method to change the sprite's color
                        def change_color(self):
                            self.image.fill(random.choice([YELLOW,MAGENTA,ORANGE,WHITE]))
                            #function to xhange the background color
                            def change_background_color():
                                global bg_color
                                bg_color=random.choice([RED,ORANGE,GREEN])
                                #create a group to hold sprite
                                all_sprites_list=pygame.sprite.Group()
                                sp1=Sprite(WHITE,20,30)
                                #RANDOMLY POSITION OF SPRITE
                                sp1.rect.x=random.randint(0,480)
                                sp1.rect.y=random.randint(0,370)


