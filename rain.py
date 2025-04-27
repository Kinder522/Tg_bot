import pygame
import random

pygame.init()

WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rain")

NUM_DROPS = 100
drops = [[random.randint(0, WIDTH), random.randint(-HEIGHT, 0)] for _ in range(NUM_DROPS)]

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    i = 0
    while i < len(drops):
        drops[i][0] += 3
        drops[i][1] += 5
        if drops[i][0] > WIDTH:
            drops[i][0] = 0
        if drops[i][1] > HEIGHT:
            drops[i][1] = 0
        i += 1

    screen.fill(BLACK)

    for drop in drops:
        pygame.draw.line(screen, WHITE, drop, (drop[0] + 3, drop[1] + 5), 2)

    pygame.display.update()
    pygame.time.delay(500)
pygame.quit()
