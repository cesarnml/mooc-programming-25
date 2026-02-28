import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

ball = pygame.image.load("ball.png")
ball_x = 0
ball_y = 0
ball_dx = 1
ball_dy = 1

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    ball_x += ball_dx
    ball_y += ball_dy

    if ball_x <= 0 or ball_x + ball.get_width() >= 640:
        ball_dx = -ball_dx
    if ball_y <= 0 or ball_y + ball.get_height() >= 480:
        ball_dy = -ball_dy

    window.fill((0, 0, 0))
    window.blit(ball, (ball_x, ball_y))
    pygame.display.flip()

    clock.tick(60)
