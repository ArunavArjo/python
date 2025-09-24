import pygame

pygame.init()
screen = pygame.display.set_mode((400,500))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        pygame.draw.rect(screen,'red',pygame.Rect(30,40,70,70))
    pygame.display.flip()

