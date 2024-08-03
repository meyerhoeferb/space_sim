import pygame
import math
from body import Body

pygame.init()

WIDTH, HEIGHT = 1000, 1000

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Solar System")

SCALE = 150 / Body.AU  # at 250, 1au = 100 pixels
TIMESTEP = 3600 * 24  # 1 day in seconds

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)
PINK = (255, 182, 193)

FONT = pygame.font.SysFont("comicsans", 16)


# 696.34 * 10**6
def main():
    run = True
    clock = pygame.time.Clock()  # clock controls how fast the game runs

    # initialize our bodies
    sun = Body("sun", 0, 0, 30, YELLOW, 1.98892 * 10**30, FONT, True)
    earth = Body(
        "earth", -1 * Body.AU, 0, 16, BLUE, 5.9742 * 10**24, FONT, i_vy=29.783 * 1000
    )
    mars = Body(
        "mars", -1.524 * Body.AU, 0, 12, RED, 6.39 * 10**23, FONT, i_vy=24.077 * 1000
    )
    mercury = Body(
        "mercury",
        0.387 * Body.AU,
        0,
        8,
        DARK_GREY,
        3.3 * 10**23,
        FONT,
        i_vy=-47.4 * 1000,
    )
    venus = Body(
        "venus",
        0.723 * Body.AU,
        0,
        14,
        PINK,
        4.8685 * 10**24,
        FONT,
        i_vy=-35.02 * 1000,
    )

    bodies = [sun, earth, mars, mercury, venus]

    while run:
        clock.tick(60)  # loop will run at most 60 times a second
        WIN.fill(BLACK)  # have to draw over last stuff each time they update

        # handle all events
        for event in pygame.event.get():
            # handle someone exiting the window
            if event.type == pygame.QUIT:
                run = False

        # render position of bodies
        for body in bodies:
            body.update_position(bodies, TIMESTEP)
            body.draw(WIN, SCALE, WIDTH, HEIGHT)

        # update screen to show changes
        pygame.display.update()

    pygame.quit()


main()
