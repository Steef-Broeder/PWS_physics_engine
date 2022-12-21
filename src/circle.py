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

	def set_velocity(self, velocity:tuple[int, int]) -> None:	
		self.velocity = velocity 

	def location(self) -> tuple[int, int]:
		return (self.x, self.y)

	def new_location(self) -> tuple[int, int]:
		new_location = (self.x + self.velocity[0], self.y + self.velocity[1])
		return new_location