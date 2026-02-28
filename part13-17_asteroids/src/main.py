# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint

pygame.init()
WINDOW_W, WINDOW_H = 640, 480
window = pygame.display.set_mode((WINDOW_W, WINDOW_H))
pygame.display.set_caption("Asteroids")

robot = pygame.image.load("robot.png")
rock = pygame.image.load("rock.png")

rw, rh = robot.get_width(), robot.get_height()
rkw, rkh = rock.get_width(), rock.get_height()

font = pygame.font.SysFont("Arial", 24)

robot_x = WINDOW_W // 2 - rw // 2
robot_y = WINDOW_H - rh

rocks = []
points = 0
game_over = False

clock = pygame.time.Clock()


# Spawn a new rock at a random x position at the top
def spawn_rock():
    rocks.append([randint(0, WINDOW_W - rkw), -rkh])


spawn_rock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if not game_over:
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            robot_x = max(robot_x - 4, 0)
        if pressed[pygame.K_RIGHT]:
            robot_x = min(robot_x + 4, WINDOW_W - rw)

        # Move rocks down
        for r in rocks:
            r[1] += 2

        # Check collisions and misses
        new_rocks = []
        for r in rocks:
            robot_rect = pygame.Rect(robot_x, robot_y, rw, rh)
            rock_rect = pygame.Rect(r[0], r[1], rkw, rkh)
            if robot_rect.colliderect(rock_rect):
                points += 1
                spawn_rock()
            elif r[1] > WINDOW_H:
                game_over = True
            else:
                new_rocks.append(r)
        rocks = new_rocks

        # Randomly spawn new rocks
        if randint(1, 50) == 1:
            spawn_rock()

    window.fill((0, 0, 0))

    for r in rocks:
        window.blit(rock, (r[0], r[1]))

    window.blit(robot, (robot_x, robot_y))

    text = font.render(f"Points: {points}", True, (255, 0, 0))
    window.blit(text, (WINDOW_W - text.get_width() - 10, 10))

    if game_over:
        over_text = font.render("Game Over!", True, (255, 0, 0))
        window.blit(
            over_text,
            (
                WINDOW_W // 2 - over_text.get_width() // 2,
                WINDOW_H // 2 - over_text.get_height() // 2,
            ),
        )

    pygame.display.flip()
    clock.tick(60)
