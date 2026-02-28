# WRITE YOUR SOLUTION HERE:
import pygame
import math
import datetime

pygame.init()
WINDOW_W, WINDOW_H = 640, 480
window = pygame.display.set_mode((WINDOW_W, WINDOW_H))

clock = pygame.time.Clock()
cx, cy = WINDOW_W // 2, WINDOW_H // 2
radius = min(cx, cy) - 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    now = datetime.datetime.now()
    hours = now.hour % 12
    minutes = now.minute
    seconds = now.second

    pygame.display.set_caption(now.strftime("%H:%M:%S"))

    window.fill((0, 0, 0))

    # Draw clock circle
    pygame.draw.circle(window, (255, 0, 0), (cx, cy), radius, 4)

    # Second hand (longest, thin)
    sec_angle = math.radians(seconds * 6 - 90)
    sec_x = cx + int(radius * 0.9 * math.cos(sec_angle))
    sec_y = cy + int(radius * 0.9 * math.sin(sec_angle))
    pygame.draw.line(window, (0, 0, 255), (cx, cy), (sec_x, sec_y), 2)

    # Minute hand (medium)
    min_angle = math.radians(minutes * 6 + seconds * 0.1 - 90)
    min_x = cx + int(radius * 0.7 * math.cos(min_angle))
    min_y = cy + int(radius * 0.7 * math.sin(min_angle))
    pygame.draw.line(window, (0, 0, 255), (cx, cy), (min_x, min_y), 4)

    # Hour hand (shortest, thick)
    hour_angle = math.radians(hours * 30 + minutes * 0.5 - 90)
    hour_x = cx + int(radius * 0.5 * math.cos(hour_angle))
    hour_y = cy + int(radius * 0.5 * math.sin(hour_angle))
    pygame.draw.line(window, (0, 0, 255), (cx, cy), (hour_x, hour_y), 6)

    # Center dot
    pygame.draw.circle(window, (255, 0, 0), (cx, cy), 6)

    pygame.display.flip()
    clock.tick(60)
