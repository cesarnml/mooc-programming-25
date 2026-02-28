# # WRITE YOUR SOLUTION HERE:
# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 0
y = 0
direction = 0  # 0=right, 1=down, 2=left, 3=up
velocity = 1
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    if direction == 0:
        x += velocity
        if x + robot.get_width() >= 640:
            direction = 1
    elif direction == 1:
        y += velocity
        if y + robot.get_height() >= 480:
            direction = 2
    elif direction == 2:
        x -= velocity
        if x <= 0:
            direction = 3
    elif direction == 3:
        y -= velocity
        if y <= 0:
            direction = 0

    clock.tick(60)
