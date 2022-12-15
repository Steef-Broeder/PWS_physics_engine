import pygame

class circle:
	def __init__(self, surface:pygame.Surface, x:int = 0, y:int = 0, color:tuple[int, int, int] = (100, 100, 100), radius:int = 10, velocity:tuple[int, int] = (0, 0)) -> None:
		self.surface = surface
		self.x = x
		self.y = y
		self.color = color
		self.radius = radius
		self.velocity = velocity

	def set_color(self, color:tuple[int, int, int]) -> None:
		self.color = color

	def draw(self):
		pygame.draw.circle(surface=self.surface, color=self.color, center=(self.x, self.y), radius=self.radius)