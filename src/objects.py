import pygame
import math

class object:
	def __init__(self, surface:pygame.Surface, x:int = 0, y:int = 0, color:tuple[int, int, int] = (100, 100, 100), mass:float = 5, velocity:tuple[int, int] = (0, 0), rotation:float = 0, acceleration:tuple[float, float] = (0, 0)) -> None:
		self.surface = surface
		self.x = x
		self.y = y
		self.color = color
		self.mass = mass
		self.velocity = velocity
		self.acceleration = acceleration 

	def set_color(self, color:tuple[int, int, int]) -> None:
		self.color = color

	def get_position(self) -> tuple[int, int]:
		return (self.x, self.y)

	def set_position(self, x:int, y:int) -> None:
		self.x = x
		self.y = y

	def get_area(self) -> float:
		return

	def update(self, deltatime:float, force:tuple[float, float] = (0, 0)) -> None:
		self.velocity = (((force[0]/self.mass) * deltatime) + self.velocity[0], ((force[1]/self.mass) * deltatime) + self.velocity[1])

	def get_applied_force(self):
		applied_force = (self.mass * self.acceleration[0], self.mass * self.acceleration[1])
		return applied_force

	def get_airresistance(self, dragcoeffient:float, area:float) -> None:
		airrestance = (0.5 * dragcoeffient * area * self.velocity[0]**2, 0.5 * dragcoeffient * area * self.velocity[1]**2)
		return airrestance


class circle(object):
	def __init__(self, surface:pygame.Surface, x:int = 0, y:int = 0, color:tuple[int, int, int] = (100, 100, 100), mass:float = 5, velocity:tuple[int, int] = (0, 0), rotation:float = 0, acceleration:tuple[float, float] = (0, 0), radius:float = 10) -> None:
		super().__init__(surface, x, y, color, mass, velocity, rotation, acceleration)
		self.dragcoeffient = 0.5
		self.radius = radius

	def draw(self):
		pygame.draw.circle(surface=self.surface, color=self.color, center=(self.x, self.y), radius=self.radius)

	def get_area(self) -> float:
		diameter = self.radius * 2
		circumference =  math.pi * diameter
		area = circumference / 2
		return area

	def get_airresistance(self) -> None:
		return super().get_airresistance(self.dragcoeffient, self.get_area())

class rect(object):
	def __init__(self, surface:pygame.Surface, x:int = 0, y:int = 0, color:tuple[int, int, int] = (100, 100, 100), mass:float = 5, velocity:tuple[int, int] = (0, 0), rotation:float = 0, acceleration:tuple[float, float] = (0, 0), width:int = 10, height:int = 10) -> None:
		super().__init__(surface, x, y, color, mass, velocity, rotation, acceleration)
		self.dragcoeffient = 1.0
		self.width = width
		self.height = height

	def draw(self):
		rectangle = pygame.Rect(self.x, self.y, self.width, self.height)
		pygame.draw.rect(surface=self.surface, color=self.color, rect=rectangle)

	def get_area(self) -> float:
		#TODO: ja deze hele teringfucntie
		return 
	
	def get_airresistance(self) -> None:
		return super().get_airresistance(self.dragcoeffient, self.get_area())