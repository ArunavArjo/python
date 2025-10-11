import pygame

pygame.init

WIDTH,HEIGHT = 600,400
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Rentangle bounce')

WHITE = ('white')
BLUE = ('blue')


rect_x = 250
rect_y = 125
rect_width = 60
rect_height = 90
rect_speed = 5

done = True
while  done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    key = pygame.key.get_pressed()



    if key[pygame.K_LEFT]:
        rect_x -= rect_speed
    if key[pygame.K_RIGHT]:
        rect_x += rect_speed
    if key[pygame.K_UP]:
        rect_y -= rect_speed
    if key[pygame.K_DOWN]:
        rect_y += rect_speed

    rect_x = max(0 ,min(WIDTH - rect_width,rect_x))
    rect_y = max(0 ,min(HEIGHT - rect_height,rect_y))

    screen.fill(WHITE)

    pygame.draw.rect(screen,BLUE,(rect_x,rect_y,rect_width,rect_height))
    pygame.display.flip()
    pygame.time.Clock().tick(90)