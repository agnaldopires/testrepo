import math
import pygame
from pygame.locals import *
from random import *

class Asteroide:
    def __init__(self, x, y, raio):
        self.x = x
        self.y = y
        self.raio = raio
        self.position = (x, y)
        self.destination = (0, 0)
        self.explosion = False
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))  # Cor aleatória para cada asteroide

    def move(self, pos, speed):
        x = pos[0]
        y = pos[1]
        if self.x > x:
            self.x -= speed
        elif self.x < x:
            self.x += speed
        if self.y > y:
            self.y -= speed
        elif self.y < y:
            self.y += speed
        self.position = (self.x, self.y)

def colisao(ast1, ast2):
    distancia = math.sqrt(((ast1.x - ast2.x) ** 2) + ((ast1.y - ast2.y) ** 2))
    if (ast1.raio + ast2.raio) >= distancia:
        return True
    else:
        return False

p = 10
m = 20
g = 30
asteroides = []
asteroides.append(Asteroide(35, 40, p))
asteroides.append(Asteroide(68, 156, m))
asteroides.append(Asteroide(90, 410, g))
asteroides.append(Asteroide(250, 20, p))
asteroides.append(Asteroide(189, 125, m))
asteroides.append(Asteroide(250, 200, g))
asteroides.append(Asteroide(120, 80, p))
asteroides.append(Asteroide(296, 260, m))
asteroides.append(Asteroide(520, 300, g))
asteroides.append(Asteroide(450, 50, p))
pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
explosionColor = (255, 0, 0)
screen.fill((255, 255, 255))
speed = 1

for asteroid in asteroides:
    xx = randint(0, 640)
    yy = randint(0, 480)
    toPosition = (xx, yy)
    asteroid.destination = toPosition
    pygame.draw.circle(screen, asteroid.color, (asteroid.x, asteroid.y), asteroid.raio, 1)

clock = pygame.time.Clock()
speed = 1

while True:
    clock.tick(30)
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
    for at in asteroides:
        if at.position == at.destination:
            destX = randint(0, 640)
            destY = randint(0, 480)
            at.destination = (destX, destY)
        at.move(at.destination, speed)
        pygame.draw.circle(screen, at.color, at.position, at.raio, 1)
    for i in range(len(asteroides)):
        for j in range(len(asteroides)):
            if asteroides[i] != asteroides[j]:
                if colisao(asteroides[i], asteroides[j]):
                    print("O asteroide %i e asteroide %i colidiram" % (i, j))
                    pygame.draw.circle(screen, explosionColor, (asteroides[i].x, asteroides[i].y), asteroides[i].raio, 1)
                    pygame.draw.circle(screen, explosionColor, (asteroides[j].x, asteroides[j].y), asteroides[j].raio, 1)
                    asteroides[i].explosion = True
                    asteroides[j].explosion = True
                    pygame.time.delay(15)
    asteroides = [ast for ast in asteroides if not ast.explosion]  # Remova os asteroides que explodiram
    if len(asteroides) == 0:
        pygame.quit()
        quit()
    pygame.display.flip()