

        if self.rect.left <=0 or self.rect.left >= 400:
            self.velocity[1] = -self.velocity[1]
            self.change_color()
            change_backround_color()

    def change_color(self):
        self.image.fill(random.choice[PURPLE,RED,GREEN,ORANGE])

def change_backround_color(self):
    global bg_color
    bg_color= random.choice[BLUE,LIGHTBLUE,BLACK]


all_sprites = pygame.sprite.Group()
sp1 = sprite(RED,20,30)
sp1.rect.x = random.randint(0,470)
sp1.rect.y = random.randint(0,380)
sp2 = sprite(RED,20,30)
sp1.rect.x = random.randint(0,470)
sp1.rect.y = random.randint(0,380)
all_sprites.add()
# Screen setup
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Bouncing Sprite")
bg_color = BLUE
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Quit on X button
            running = False

    # Update
    all_sprites.update()
    screen.fill(bg_color)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(120)  # frame rate

pygame.quit()
