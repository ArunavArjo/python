import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
screen.fill == 'blue'

pygame.draw.circle(screen ,'green', (300,300),50)
pygame.draw.circle(screen ,'blue' ,(100,100),50,3)
pygame.display.update()
running = True
while  running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
            pygame.quit()