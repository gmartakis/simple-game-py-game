"""
 Simple graphics demo

 Sample Python/Pygame Programs
 version 1.0
 author: Ioannis Martakis	

"""

#Import a library of functions called 'pygame'
import pygame, sys, glob
import os
import time
import turtle

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

pygame.init()
screen = pygame.display.set_mode((1118, 506))
done = False
clock = pygame.time.Clock()

x_coor = 620
y_coor = 73

#[10, 4.52]
speed_x = 10
speed_y = 4.52

counter = 0

def animate(x,y):
    for z in range(0, 10):
        print('animation')
        x = x-10
        y = y+4.52

while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     done = True
                elif event.type == pygame.MOUSEMOTION:
                    (mouseX, mouseY) = pygame.mouse.get_pos()
                    #print(mouseX, mouseY)


                screen.fill((255, 255, 255))
                largeImage = get_image('background.png')
                Rectbutton = get_image('objectimage.png')
                screen.blit(largeImage, (20, 20))
                rect_image = screen.blit(Rectbutton, (x_coor, y_coor))

                ballrect = Rectbutton.get_rect()

                #rect_image1 = screen.blit(Rectbutton, (100, 308))
                b = pygame.draw.rect(screen, BLUE, [700, 250, 115, 50], 2)
                font = pygame.font.SysFont('Calibri', 25, True, False)
                text = font.render("ANIMATE", True, BLUE)
                screen.blit(text, (707, 264))

                # If the sprite goes off the edge of the screen,
                # make it move in the opposite direction

               if event.type == pygame.MOUSEBUTTONDOWN:
                   if event.button == 1:
                       x, y = event.pos
                       if b.collidepoint(x, y):
                        x_coor = x_coor-speed_x
                        y_coor = y_coor+speed_y
                        animate(x_coor,y_coor)
                        print("x: " , x_coor)
                        print("y: " , y_coor)
            pygame.display.update()
            clock.tick(60)

pygame.quit()
