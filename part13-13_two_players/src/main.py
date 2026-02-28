# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
WINDOW_W, WINDOW_H = 640, 480
window = pygame.display.set_mode((WINDOW_W, WINDOW_H))


class Robot:
    def __init__(self, image, x, y, keys):
        self.image = image
        self.x = x
        self.y = y
        self.keys = keys  # dict: {left, right, up, down}

    def update(self, pressed):
        if pressed[self.keys["left"]]:
            self.x = max(self.x - 2, 0)
        if pressed[self.keys["right"]]:
            self.x = min(self.x + 2, WINDOW_W - self.image.get_width())
        if pressed[self.keys["up"]]:
            self.y = max(self.y - 2, 0)
        if pressed[self.keys["down"]]:
            self.y = min(self.y + 2, WINDOW_H - self.image.get_height())

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))


robot_img = pygame.image.load("robot.png")
rw, rh = robot_img.get_width(), robot_img.get_height()

player1 = Robot(
    robot_img,
    200 - rw / 2,
    200 - rh / 2,
    {
        "left": pygame.K_LEFT,
        "right": pygame.K_RIGHT,
        "up": pygame.K_UP,
        "down": pygame.K_DOWN,
    },
)

player2 = Robot(
    robot_img,
    440 - rw / 2,
    300 - rh / 2,
    {"left": pygame.K_a, "right": pygame.K_d, "up": pygame.K_w, "down": pygame.K_s},
)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()
    player1.update(keys)
    player2.update(keys)

    window.fill((0, 0, 0))
    player1.draw(window)
    player2.draw(window)
    pygame.display.flip()

    clock.tick(60)
