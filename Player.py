import pygame
from pygame.locals import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.life = 5
        self.image = pygame.transform.scale(pygame.image.load('m.png'), (25, 25))
        self.surf = pygame.Surface((25, 25))
        self.rect = self.surf.get_rect()
        self.rect.centerx = 350
        self.rect.centery = 549
        self.paths = []
        self.vertices = []
        self.prevKey = None
        self.keycount = sum(pygame.key.get_pressed())

    def move(self, screen, pressed_keys):
        scrsurf1 = screen.get_at((self.rect.centerx - 1, self.rect.centery))  # left
        scrsurf2 = screen.get_at((self.rect.centerx + 1, self.rect.centery))  # right
        scrsurf3 = screen.get_at((self.rect.centerx, self.rect.centery - 1))  # top
        scrsurf4 = screen.get_at((self.rect.centerx, self.rect.centery + 1))  # bottom

        if pressed_keys[K_UP] and scrsurf3 == (255, 255, 255, 255):
            self.rect.move_ip(0, -1)
        if pressed_keys[K_DOWN] and scrsurf4 == (255, 255, 255, 255):
            self.rect.move_ip(0, 1)
        if pressed_keys[K_LEFT] and scrsurf1 == (255, 255, 255, 255):
            self.rect.move_ip(-1, 0)
        if pressed_keys[K_RIGHT] and scrsurf2 == (255, 255, 255, 255):
            self.rect.move_ip(1, 0)

    def push(self, screen, pressed_keys):
        if sum(pressed_keys) - self.keycount == 1:
            scrsurf1 = screen.get_at((self.rect.centerx - 1, self.rect.centery))  # left
            scrsurf2 = screen.get_at((self.rect.centerx + 1, self.rect.centery))  # right
            scrsurf3 = screen.get_at((self.rect.centerx, self.rect.centery - 1))  # top
            scrsurf4 = screen.get_at((self.rect.centerx, self.rect.centery + 1))  # bottom

            if pressed_keys[K_UP] and self.rect.centery > 150 and scrsurf3 != (0, 128, 128, 255):
                self.rect.move_ip(0, -1)

            if pressed_keys[K_DOWN] and self.rect.centery < 550 and scrsurf4 != (0, 128, 128, 255):
                self.rect.move_ip(0, 1)

            if pressed_keys[K_LEFT] and self.rect.centerx > 150 and scrsurf1 != (0, 128, 128, 255):
                self.rect.move_ip(-1, 0)

            if pressed_keys[K_RIGHT] and self.rect.centerx < 550 and scrsurf2 != (0, 128, 128, 255):
                self.rect.move_ip(1, 0)

    def setTempPath(self, temp):
        if self.rect.center not in temp:
            temp.append(self.rect.center)

    def setTempVertex(self, temp, key):
        if key != self.prevKey and self.rect.center not in temp and (
                key or self.prevKey) != pygame.K_SPACE:  # do not duplicate vertex if same key is pressed again
            temp.append(self.rect.center)
            self.prevKey = key

    def setPath(self, temp):
        self.paths.append(temp)

    def setVertices(self, temp):
        self.vertices.append(temp)

    def search(self, temp, last):
        # case 1: we have a complete polygon
        # case 2: 2 verticies
        # case 3: > 2 verticies but incomplete
        # Additional:
        #  - consider the outer edges as well
        x = [(150, 150), (549, 150), (549, 549), (150, 549)]
        vert = self.vertices.copy()
        sorted_temp_x = sorted(temp, key=lambda x: x[0], reverse=True)
        sorted_temp_y = sorted(temp, key=lambda x: x[1], reverse=True)
        max_x, max_y = sorted_temp_x[0][0], sorted_temp_y[0][1]
        min_x, min_y = sorted_temp_x[-1][0], sorted_temp_y[-1][1]
        # print(max_x,max_y,min_x,min_y)
        found = False
        first = temp[0]

        if len(temp) == 2:
            if first[0] == (150 or 549) and last[0] == (549 or 150):
                if last[1] > 279:
                    temp += [(549, 549), (150, 549)]
                else:
                    temp += [(549, 150), (150, 150)]
            if first[1] == (549 or 150) and last[1] == (150 or 150):
                if last[0] < 279:
                    temp += [(150, 150), (150, 549)]
                else:
                    temp += [(549, 150), (549, 549)]

        x = [(150, 150), (549, 150), (549, 549), (150, 549)]
        for nextvert in x:
            if last[0] == nextvert[0] or last[1] == nextvert[1]:
                if ((min_x <= nextvert[0] <= max_x) and (min_y <= nextvert[1] <= max_y)):
                    temp.append(nextvert)
                    last = nextvert

        for i in range(len(vert)):
            nextvert = vert[i]
            for x in range(len(nextvert)):
                if last[0] == nextvert[x][0] or last[1] == nextvert[x][1]:
                    if ((min_x <= nextvert[x][0] <= max_x) and (min_y <= nextvert[x][1] <= max_y)) or found == True:
                        temp.append(nextvert[x])
                        last = nextvert[x]
                        found = True
                    if len(temp) <= 2:
                        temp.append(nextvert[x])
                        last = nextvert[x]
                    if first[0] == nextvert[x][0] or first[1] == nextvert[x][1]:
                        break

    def get_life(self):
        return self.life

    def coll(self, x1, y1, x2, y2):
        if abs(x1 - x2) <= 15 and abs(y1 - y2) <= 15:
            self.lifeDecrease()
            return True

    def lifeDecrease(self):
        self.life = self.life - 1