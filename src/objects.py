import pygame

class object:
	def __init__(self, surface:pygame.Surface, x:int, y:int, color:tuple[int, int, int], mass:float, velocity:tuple[int, int], force:tuple[int, int]) -> None:
		self.surface = surface
		self.x = x
		self.y = y
		self.color = color
		self.mass = mass
		self.velocity = velocity
		self.force = force

	def set_color(self, color:tuple[int, int, int]) -> None:
		self.color = color

	def get_position(self) -> tuple[int, int]:
		return (self.x, self.y)

	def set_position(self, x:int, y:int) -> None:
		self.x = x
		self.y = y

	def apply_force(self, deltatime:float) -> None:
		return
		##self.velocity = (self.mass * self.apply_force[0] * deltatime, self.mass * self.apply_force[1] * deltatime)


class circle(object):
	def __init__(self, surface:pygame.Surface, x:int, y:int, color:tuple[int, int, int], mass:float, velocity:tuple[int, int], force:tuple[int, int], radius:int) -> None:
		super().__init__(surface, x, y, color, mass, velocity, force)
		self.radius = radius

	def draw(self):
		pygame.draw.circle(surface=self.surface, color=self.color, center=(self.x, self.y), radius=self.radius)

class rect(object):
	def __init__(self, surface:pygame.Surface, x:int, y:int, color:tuple[int, int, int], mass:float, velocity:tuple[int, int], force:tuple[int, int], width:int, height:int) -> None:
		super().__init__(surface, x, y, color, mass, velocity, force)
		self.width = width
		self.height = height

	def draw(self):
		rectangle = pygame.Rect(self.x, self.y, self.width, self.height)
		pygame.draw.rect(surface=self.surface, color=self.color, rect=rectangle)
