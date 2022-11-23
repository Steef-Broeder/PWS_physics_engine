import pygame

# class object:
#     def __init__(self, surface:pygame.Surface, x:int, y:int, color:tuple, mass:float, speed:int, friction:float, gravity:bool) -> None:
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
#     def __init__(self, surface:pygame.Surface, x: int, y: int, color: tuple, mass: float, speed:int, friction: float, gravity: bool, width:int, height:int) -> None:
#         super().__init__(surface, x, y, color, mass, speed, friction, gravity)
#         self.width = width
#         self.height = height

#     def draw(self):
#         rectangle = pygame.Rect(self.x, self.y, self.width, self.height)
#         pygame.draw.rect(surface=self.surface, color=self.color, rect=rectangle)


# class circle(object):
#     def __init__(self, surface:pygame.Surface, x: int, y: int, color: tuple, mass: float, speed:int, friction: float, gravity: bool, radius:int) -> None:
#         super().__init__(surface, x, y, color, mass, speed, friction, gravity)
#         self.radius = radius
	
#     def draw(self):
#         pygame.draw.circle(surface=self.surface, color=self.color, center=(self.x, self.y), radius=self.radius)


# class object:
#     def __init__(self, surface:pygame.Surface, x:int, y:int, color:tuple) -> None:
#         self.surface = surface
#         self.x = x
#         self.y = y
#         self.color = color

#     def set_position(self, x, y):
#         self.x = x
#         self.y = y

#     def set_color(self, color:tuple):
#         self.color = color

# class rect(object):
#     def __init__(self, surface:pygame.Surface, x: int, y: int, color: tuple, width:int, height:int) -> None:
#         super().__init__(surface, x, y, color)
#         self.width = width
#         self.height = height

#     def draw(self):
#         rectangle = pygame.Rect(self.x, self.y, self.width, self.height)
#         pygame.draw.rect(surface=self.surface, color=self.color, rect=rectangle)


# class circle(object):
#     def __init__(self, surface:pygame.Surface, x: int, y: int, color: tuple, radius:int) -> None:
#         super().__init__(surface, x, y, color)
#         self.radius = radius
	
#     def draw(self):
#         pygame.draw.circle(surface=self.surface, color=self.color, center=(self.x, self.y), radius=self.radius)

class circle():
	def __init__(self, surface:pygame.Surface, x:int, y:int, color:tuple, radius:int) -> None:
		self.surface = surface
		self.x = x
		self.y = y
		self.color = color
		self.radius = radius
	def draw(self):
		pygame.draw.circle(surface=self.surface, color=self.color, center=(self.x, self.y), radius=self.radius)