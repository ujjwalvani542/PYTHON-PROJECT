import pygame
import time
import random

pygame.init()

# Window Setup
WIDTH, HEIGHT = 542, 566
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

# Game Constants
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 50
PLAYER_VELOCITY = 5  # Increased slightly for better gameplay responsiveness

STAR_WIDTH = 20
STAR_HEIGHT = 20
STAR_VELOCITY = 4

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Load Background (Falls back to black if space.jpg is missing)
try:
    BG = pygame.image.load("space.jpg")
    BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))
except pygame.error:
    BG = pygame.Surface((WIDTH, HEIGHT))
    BG.fill((0, 0, 0))

FONT = pygame.font.SysFont("sans-serif", 40)

def draw(player, elapsed_time, stars):
    WIN.blit(BG, (0, 0))
    
    # Draw Player
    pygame.draw.rect(WIN, RED, player)
    
    # Draw Stars
    for star in stars:
        pygame.draw.rect(WIN, YELLOW, star)
        
    # Draw Timer
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", True, WHITE)
    WIN.blit(time_text, (10, 10))
    
    pygame.display.update()

def main():
    run = True
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    start_time = time.time()
    
    star_add_increment = 2000  # milliseconds
    star_count = 0
    stars = []
    
    while run:
        # Track time passed since last frame to increment star spawn counter
        star_count += clock.tick(60) 
        elapsed_time = time.time() - start_time
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        # Spawn new stars after the increment time passes
        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)
            
            # Decrease increment over time to make the game progressively harder
            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0
            
        # Player Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VELOCITY >= 0:
            player.x -= PLAYER_VELOCITY
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VELOCITY + PLAYER_WIDTH <= WIDTH:
            player.x += PLAYER_VELOCITY
            
        # Move stars and handle collisions
        for star in stars[:]:
            star.y += STAR_VELOCITY
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.colliderect(player):
                # End game on collision
                print(f"Game Over! You survived for {round(elapsed_time)} seconds.")
                run = False
                
        draw(player, elapsed_time, stars)
        
    pygame.quit()

if __name__ == "__main__":
    main()
