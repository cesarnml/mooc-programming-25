# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint

pygame.init()
WINDOW_W, WINDOW_H = 640, 480
window = pygame.display.set_mode((WINDOW_W, WINDOW_H))

robot = pygame.image.load("robot.png")
rw = robot.get_width()
rh = robot.get_height()

x = randint(0, WINDOW_W - rw)
y = randint(0, WINDOW_H - rh)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = event.pos
            if x <= mx <= x + rw and y <= my <= y + rh:
                x = randint(0, WINDOW_W - rw)
                y = randint(0, WINDOW_H - rh)

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    clock.tick(60)
