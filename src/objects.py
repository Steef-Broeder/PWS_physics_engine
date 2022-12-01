import pygame

# class object:
#     def __init__(self, surface:pygame.Surface, x:int, y:int, color:tuple, mass:float, speed:int, friction:float, gravity:tuple) -> None:
#         self.surface = surface
#         self.x = x
#         self.y = y
#         self.color = color
#         self.mass = mass
#         self.speed = speed
#         self.friction = friction
#         self.gravity = gravity

#     def set_position(self, x, y):
#         self.x = x
#         self.y = y

# class rect(object):
#     def __init__(self, surface:pygame.Surface, x: int, y: int, color: tuple, mass: float, speed:int, friction: float, gravity: tuple, width:int, height:int) -> None:
#         super().__init__(surface, x, y, color, mass, speed, friction, gravity)
#         self.width = width
#         self.height = height

#     def draw(self):
#         rectangle = pygame.Rect(self.x, self.y, self.width, self.height)
#         pygame.draw.rect(surface=self.surface, color=self.color, rect=rectangle)


# class circle(object):
#     def __init__(self, surface:pygame.Surface, x: int, y: int, color: tuple, mass: float, speed:int, friction: float, gravity: tuple, radius:int) -> None:
#         super().__init__(surface, x, y, color, mass, speed, friction, gravity)
#         self.radius = radius
	
#     def draw(self):
#         pygame.draw.circle(surface=self.surface, color=self.color, center=(self.x, self.y), radius=self.radius)


class object:
	def __init__(self, surface:pygame.Surface, x:int, y:int, color:tuple, mass:float, velocity:tuple, global_force:tuple) -> None:
		self.surface = surface
		self.x = x
		self.y = y
		self.color = color
		self.mass = mass
		self.velocity = velocity
		self.global_force = global_force

	def set_color(self, color:tuple) -> None:
		self.color = color

	def get_position(self) -> tuple:
		return (self.x, self.y)

	def set_position(self, x:int, y:int) -> None:
		self.x = x
		self.y = y

	def apply_force(self, deltatime:float) -> None:
		self.velocity = (self.mass * self.apply_force[0] * deltatime, self.mass * self.apply_force[1] * deltatime)


class circle(object):
	def __init__(self, surface:pygame.Surface, x:int, y:int, mass:float, velocity:float, global_force:tuple, color:tuple, radius:int) -> None:
		super().__init__(surface, x, y, color, mass, velocity, global_force)
		self.radius = radius

	def draw(self):
		pygame.draw.circle(surface=self.surface, color=self.color, center=(self.x, self.y), radius=self.radius)

class rect(object):
	def __init__(self, surface:pygame.Surface, x:int, y:int, mass:float, velocity:float, global_force:tuple, color:tuple, width:int, height:int) -> None:
		super().__init__(surface, x, y, color, mass, velocity, global_force)
		self.width = width
		self.height = height

	def draw(self):
		rectangle = pygame.Rect(self.x, self.y, self.width, self.height)
		pygame.draw.rect(surface=self.surface, color=self.color, rect=rectangle)
