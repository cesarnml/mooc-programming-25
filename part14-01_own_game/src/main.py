# A collecting game
# The player moves the robot with the arrow keys.
# A coin appears in a random location on the screen. When the robot reaches it, the coin moves to a new location.
# There are also monsters on the screen, and the robot must avoid them.

import pygame
import random

pygame.init()

WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

robot = pygame.image.load("robot.png")
coin = pygame.image.load("coin.png")
monster = pygame.image.load("monster.png")

robot_w, robot_h = robot.get_size()
coin_w, coin_h = coin.get_size()
monster_w, monster_h = monster.get_size()

font = pygame.font.SysFont("Arial", 24)


def random_pos(img_w, img_h):
    return [random.randint(0, WIDTH - img_w), random.randint(0, HEIGHT - img_h)]


robot_x = WIDTH / 2 - robot_w / 2
robot_y = HEIGHT / 2 - robot_h / 2
speed = 4

coin_pos = random_pos(coin_w, coin_h)
score = 0

num_monsters = 2
monsters = []
monster_dirs = []
for _ in range(num_monsters):
    monsters.append(random_pos(monster_w, monster_h))
    monster_dirs.append([random.choice([-2, 2]), random.choice([-2, 2])])

game_over = False
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            robot_x = max(0, robot_x - speed)
        if keys[pygame.K_RIGHT]:
            robot_x = min(WIDTH - robot_w, robot_x + speed)
        if keys[pygame.K_UP]:
            robot_y = max(0, robot_y - speed)
        if keys[pygame.K_DOWN]:
            robot_y = min(HEIGHT - robot_h, robot_y + speed)

        robot_rect = pygame.Rect(robot_x, robot_y, robot_w, robot_h)
        coin_rect = pygame.Rect(coin_pos[0], coin_pos[1], coin_w, coin_h)
        if robot_rect.colliderect(coin_rect):
            score += 1
            coin_pos = random_pos(coin_w, coin_h)

        for i in range(num_monsters):
            monsters[i][0] += monster_dirs[i][0]
            monsters[i][1] += monster_dirs[i][1]
            if monsters[i][0] <= 0 or monsters[i][0] >= WIDTH - monster_w:
                monster_dirs[i][0] *= -1
            if monsters[i][1] <= 0 or monsters[i][1] >= HEIGHT - monster_h:
                monster_dirs[i][1] *= -1

            monster_rect = pygame.Rect(
                monsters[i][0], monsters[i][1], monster_w, monster_h
            )
            if robot_rect.colliderect(monster_rect):
                game_over = True

    screen.fill((50, 50, 50))
    screen.blit(coin, coin_pos)
    for m in monsters:
        screen.blit(monster, m)
    screen.blit(robot, (robot_x, robot_y))

    score_text = font.render(f"Score: {score}", True, (255, 255, 0))
    screen.blit(score_text, (10, 10))

    if game_over:
        over_text = font.render("GAME OVER! Press ESC to quit", True, (255, 0, 0))
        screen.blit(over_text, (WIDTH // 2 - over_text.get_width() // 2, HEIGHT // 2))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
