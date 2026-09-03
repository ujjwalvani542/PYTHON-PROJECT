import pygame
import time
import random

pygame.init()

WIDTH, HEIGHT = 542, 566
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 50

PLAYER_VELOCITY=2

BG = pygame.image.load("space.jpg")


def draw(player):
    WIN.blit(BG, (0, 0))
    pygame.draw.rect(WIN, "red", player)

   
    pygame.display.update()


def main():
    run = True

    player = pygame.Rect(
        200,
        HEIGHT - PLAYER_HEIGHT,
        PLAYER_WIDTH,
        PLAYER_HEIGHT
    )


    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x-=PLAYER_VELOCITY
        if keys[pygame.K_RIGHT]:

            player.x+=PLAYER_VELOCITY
        draw(player)

    pygame.quit()


if __name__ == '__main__':
    main()
