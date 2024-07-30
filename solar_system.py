import pygame
import math

pygame.init()

WIDTH, HEIGHT = 1000, 1000

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Solar System")


def main():
    run = True
    clock = pygame.time.Clock()  # clock controls how fast the game runs

    while run:
        clock.tick(60)  # loop will run at most 60 times a second
        # handle all events
        for event in pygame.event.get():
            # handle someone exiting the window
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()


main()
