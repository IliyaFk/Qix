import pygame
from Player import Player
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_SPACE,
    KEYDOWN,
    QUIT,
)
from pygame.locals import *

class main:
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 900

    initial = ((100,80),(100,560),(700,560),(700, 80))

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    player = Player()

    player.polygon.x = 90
    player.polygon.y = 550


    running = True

    while running:

        for event in pygame.event.get():

            if event.type == KEYDOWN:

                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_SPACE:
                    initial = ((100,80),(100,560),(600,560),(600,450),(710, 450),(710, 80))

            elif event.type == QUIT:
                running = False

        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        screen.fill((0, 0, 0))
        field = pygame.draw.polygon(screen, [0,0,255], initial,2)
        screensurf = screen.get_at((player.polygon.x, player.polygon.y))
        print(screensurf)
        #player.polygon.clamp_ip(field)   #This will keep the player on the board
        screen.blit(player.surf, player.polygon)

        pygame.display.flip()

    pygame.quit()