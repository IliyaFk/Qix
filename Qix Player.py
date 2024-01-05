import pygame

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

initial = ((100,80),(100,560),(700,560),(700, 80))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -1)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 1)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1, 0)

        if self.rect.left < initial[0][0] - 10:
            self.rect.left = initial[0][0] - 10

        # if self.rect.right < initial[2][0] + 10 and self.rect.right > initial [2][0] + 8:
        #     if self.rect.top > initial[0][1] - 10:
        #         if self.rect.bottom != initial[1][1] + 10:
        #             print(self.rect.left)
        #             self.rect.right = initial[2][0] + 10

        if self.rect.right > initial[2][0] + 10:
            self.rect.right = initial[2][0] + 10

        if self.rect.top <= initial[0][1] - 10:
            self.rect.top = initial[0][1] - 10

        # if self.rect.top > initial[0][1] - 10 and self.rect.top < initial[0][1] - 8:
        #     if self.rect.left != initial[0][0] - 10:
        #         if self.rect.right != initial[2][0] + 10:
        #             if self.rect.bottom < initial[1][1] + 10:
        #                 self.rect.top = initial[0][1] - 10

        if self.rect.bottom >= initial[1][1] + 10:
            self.rect.bottom = initial[1][1] + 10

        # if self.rect.bottom < initial[1][1] + 10 and self.rect.bottom > initial[1][1] + 8:
        #     if self.rect.left != initial[0][0] - 10:
        #         if self.rect.right != initial[2][0] + 10:
        #             self.rect.bottom = initial[1][1] + 10