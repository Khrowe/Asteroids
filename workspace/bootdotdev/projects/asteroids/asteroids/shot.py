import pygame
from constants import SHOT_RADIUS, LINE_WIDTH, WHITE
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)

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