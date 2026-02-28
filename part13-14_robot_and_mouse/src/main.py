# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
WINDOW_W, WINDOW_H = 640, 480
window = pygame.display.set_mode((WINDOW_W, WINDOW_H))

robot = pygame.image.load("robot.png")
rw = robot.get_width()
rh = robot.get_height()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    mouse_x, mouse_y = pygame.mouse.get_pos()
    x = mouse_x - rw / 2
    y = mouse_y - rh / 2

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    clock.tick(60)
