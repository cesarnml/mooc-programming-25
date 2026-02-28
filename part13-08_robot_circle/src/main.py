# WRITE YOUR SOLUTION HERE:
import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
w = robot.get_width()
h = robot.get_height()

angle = 0
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))

    for i in range(10):
        a = angle + i * (2 * math.pi / 10)
        x = 320 + math.cos(a) * 150 - w / 2
        y = 240 + math.sin(a) * 150 - h / 2
        window.blit(robot, (x, y))

    pygame.display.flip()

    angle += 0.01
    clock.tick(60)
