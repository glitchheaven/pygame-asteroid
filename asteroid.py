import pygame
from circleshape import CircleShape
import random
from constants import *



class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, surface):
		#or (screen, "white", self.position, self.radius, 2)

		pygame.draw.circle(surface, (255, 255, 255), (self.position.x, self.position.y), self.radius, 2)

	def update(self, dt):
		#self.position += self.velocity * dt
		self.position.y += self.velocity.y * dt
		self.position.x += self.velocity.x * dt

	def split(self):
		self.kill()
		if (self.radius <= ASTEROID_MIN_RADIUS):
			return
		angle = random.uniform(20, 50)
		rotated_v1 = self.velocity.rotate(angle)
		rotated_v2 = self.velocity.rotate(-angle)

		new_radius = self.radius - ASTEROID_MIN_RADIUS

		
		asteroid = Asteroid(self.position.x, self.position.y, new_radius)
		asteroid.velocity = rotated_v1 * 1.2
		asteroid = Asteroid(self.position.x, self.position.y, new_radius)
		asteroid.velocity = rotated_v2 * 1.2


