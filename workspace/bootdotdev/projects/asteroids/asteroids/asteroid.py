import pygame
from constants import ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE_SECONDS, ASTEROID_MAX_RADIUS, LINE_WIDTH, WHITE
from circleshape import CircleShape
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        self.rotation = 0

    def draw (self, screen):
        pygame.draw.circle(
            screen, 
            WHITE,
            self.position,
            self.radius, 
            LINE_WIDTH
            )
    
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        else:
            direction = random.uniform(20,50)
            new_vector_1 = self.velocity.rotate(direction)
            new_vector_2 = self.velocity.rotate(-direction)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid_1 = Asteroid(
                self.position.x,
                self.position.y,
                new_radius
            )

            asteroid_2 = Asteroid(
                self.position.x,
                self.position.y,
                new_radius
            )

            asteroid_1.velocity = new_vector_1 * 1.2
            asteroid_2.velocity = new_vector_2



