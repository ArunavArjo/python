import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Two Sprites with Custom Event")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Custom Event Type
SPRITE_INTERACTION_EVENT = pygame.USEREVENT + 1

# Custom Sprite Class
class MySprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y, size):
        super().__init__()
        self.image = pygame.Surface([size, size])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        # Sprites can have their own update logic
        pass

# Create sprites
sprite1 = MySprite(RED, 200, 300, 50)
sprite2 = MySprite(BLUE, 600, 300, 50)

# Create a sprite group and add sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1)
all_sprites.add(sprite2)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Post a custom event when spacebar is pressed
                pygame.event.post(pygame.event.Event(SPRITE_INTERACTION_EVENT, message="Spacebar pressed!"))

        if event.type == SPRITE_INTERACTION_EVENT:
            print(f"Custom Event Triggered: {event.message}")
            # Example: Change sprite color upon custom event
            sprite1.image.fill((0, 255, 0)) # Green
            sprite2.image.fill((255, 255, 0)) # Yellow

    # Update sprites (if they have update logic)
    all_sprites.update()

    # Drawing
    screen.fill(WHITE)  # Clear screen with white background
    all_sprites.draw(screen) # Draw all sprites in the group

    pygame.display.flip() # Update the display

pygame.quit()