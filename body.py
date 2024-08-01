from __future__ import annotations

from typing import Tuple, List
import pygame
import math


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
        i_vx: float = 0,
        i_vy: float = 0,
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

        self.x_vel = i_vx  # in m/s
        self.y_vel = i_vy

    def draw(self, win: pygame.Surface, scale: float, w: int, h: int):
        # scale the current position and center on window
        curr_x = self.x * scale + w / 2
        curr_y = self.y * scale + h / 2

        # draw orbital path
        if len(self.orbit) >= 2:
            to_draw_orbit = []
            for point in self.orbit:
                x, y = point
                x = x * scale + w / 2
                y = y * scale + h / 2
                to_draw_orbit.append((x, y))

            pygame.draw.lines(win, self.color, False, to_draw_orbit, 2)

        pygame.draw.circle(win, self.color, (curr_x, curr_y), self.radius)

    def attraction(self, other: Body) -> Tuple[float, float]:
        """calculate the force of attraction in x and y direction between this body and some other body

        Args:
            other (Body): body to calculate force to

        Returns:
            Tuple[float, float]: force in x dir, force in y dir
        """
        # calculate distance between objects
        distance_x = other.x - self.x
        distance_y = other.y - self.y

        distance = math.sqrt(distance_x**2 + distance_y**2)

        if other.sun:
            self.distance_to_sun = distance

        # calculate force between objects in x and y direction
        force = self.G * self.mass * other.mass / distance**2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force

        return force_x, force_y

    def update_position(self, bodies: List[Body], timestep: int):
        total_fx = total_fy = 0
        for b in bodies:
            if self == b:
                continue

            fx, fy = self.attraction(b)

            total_fx += fx
            total_fy += fy

        self.x_vel += total_fx / self.mass * timestep
        self.y_vel += total_fy / self.mass * timestep

        self.x += self.x_vel * timestep
        self.y += self.y_vel * timestep

        # keep it at just last n positions
        if len(self.orbit) > 50:
            self.orbit.pop(0)
        self.orbit.append((self.x, self.y))
