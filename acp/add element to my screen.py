import pygame
pygame.init()

screen = pygame.display.set_mode((400, 500))
pygame.display.set_caption("Pygame Text Example") 


font = pygame.font.SysFont('Arial', 30) 

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

   
    screen.fill((0, 0, 0)) 

    pygame.draw.rect(screen, 'red', pygame.Rect(30, 40, 70, 70))

    
    text_surface = font.render('Hello Pygame!', True, (255, 255, 255)) # White text

    
    screen.blit(text_surface, (100, 200))
    pygame.display.flip()

pygame.quit() 