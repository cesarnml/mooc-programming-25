# WRITE YOUR SOLUTION HERE:
import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
robot_w = robot.get_width()
robot_h = robot.get_height()

clock = pygame.time.Clock()

# Each robot: [x, y, dx] where dx is horizontal speed (0 while falling, ±1 on ground)
robots = []
spawn_timer = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    spawn_timer += 1
    if spawn_timer >= 50:
        spawn_timer = 0
        x = random.randint(0, 640 - robot_w)
        robots.append([x, -robot_h, 0])

    # Update robots
    for r in robots:
        if r[2] == 0:
            r[1] += 1
            if r[1] + robot_h >= 480:
                r[1] = 480 - robot_h
                r[2] = random.choice([-1, 1])
        else:
            r[0] += r[2]

    robots = [r for r in robots if -robot_w < r[0] < 640]

    window.fill((0, 0, 0))
    for r in robots:
        window.blit(robot, (r[0], r[1]))
    pygame.display.flip()

    clock.tick(60)
