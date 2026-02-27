# WRITE YOUR SOLUTION HERE:
# WRITE YOUR SOLUTION HERE:

import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
width = robot.get_width()
height = robot.get_height()

window.fill((0, 0, 0))
for _ in range(1000):
    x_offset = random.randint(0, 640 - width - 10)
    y_offset = random.randint(0, 480 - height)
    window.blit(robot, (x_offset, y_offset))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
