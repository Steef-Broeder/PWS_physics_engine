import pygame

class object:
	def __init__(self, surface:pygame.Surface, x:int, y:int, color:tuple[int, int, int], mass:float = 5, velocity:tuple[int, int] = (0, 0), force:tuple[int, int] = (0, 0), acceleration_variable:int = 9.81) -> None:
		self.surface = surface
		self.x = x
		self.y = y
		self.color = color
		self.mass = mass
		self.velocity = velocity
		self.force = force
		self.acceleration_variable = acceleration_variable

	def set_color(self, color:tuple[int, int, int]) -> None:
		self.color = color

	def get_position(self) -> tuple[int, int]:
		return (self.x, self.y)

	def set_position(self, x:int, y:int) -> None:
		self.x = x
		self.y = y

	def get_aantrekkingskracht(self):
		self.aantrekkingskracht = self.mass * self.acceleration_variable

	def update(self, deltatime:float) -> None:
		self.velocity = (((self.force[0]/self.mass) * deltatime) + self.velocity[0], ((self.force[1]/self.mass) * deltatime) + self.velocity[1])


class circle(object):
	def __init__(self, surface:pygame.Surface, x:int, y:int, color:tuple[int, int, int], mass:float = 5, velocity:tuple[int, int] = (0, 0), force:tuple[int, int] = (0, 0), radius:float = 10) -> None:
		super().__init__(surface, x, y, color, mass, velocity, force)
		self.radius = radius

	def draw(self):
		pygame.draw.circle(surface=self.surface, color=self.color, center=(self.x, self.y), radius=self.radius)

class rect(object):
	def __init__(self, surface:pygame.Surface, x:int, y:int, color:tuple[int, int, int], mass:float = 5, velocity:tuple[int, int] = (0, 0), force:tuple[int, int] = (0, 0), width:int = 10, height:int = 10) -> None:
		super().__init__(surface, x, y, color, mass, velocity, force)
		self.width = width
		self.height = height

	def draw(self):
		rectangle = pygame.Rect(self.x, self.y, self.width, self.height)
		pygame.draw.rect(surface=self.surface, color=self.color, rect=rectangle)
