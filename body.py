from typing import Tuple
import pygame


class Body:
    AU = 149.6e6 * 1000  # 1 AU in m
    G = 6.67428e-11

    def __init__(
        self,
        x: float,
        y: float,
        radius: float,
        color: Tuple[int],
        mass: float,
        is_sun: bool = False,
    ) -> None:
        self.x = x
        self.y = y
        self.radius = radius  # r of body in m
        self.color = color
        self.mass = mass  # mass of body in kg

        self.orbit = []  # track points body has occupied so can draw them
        self.sun = is_sun  # is this the sun
        self.distance_to_sun = 0  # in AU

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win: pygame.Surface, scale: float, w: int, h: int):
        # scale the current position and center on window
        x = self.x * scale + w / 2
        y = self.y * scale + h / 2

        pygame.draw.circle(win, self.color, (x, y), self.radius)
