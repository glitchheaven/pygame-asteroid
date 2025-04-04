import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
  pygame.init()
  print("Starting Asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


  clock = pygame.time.Clock()
  dt = 0
  asteroids = pygame.sprite.Group()
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  Shot.containers = (shots, updatable, drawable)
  Player.containers = (updatable, drawable)
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable)

  asteroidfield = AsteroidField()
  playerChar = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
    #clear the screen
    screen.fill("black")
    #playerChar.update(dt)
    updatable.update(dt)
    
    #draw the player and other elements
    #playerChar.draw(screen)
    for entity in drawable:
      entity.draw(screen)
    #Update the displayer after drawing
    for asteroid in asteroids:
      for bullet in shots:
        dx = asteroid.position.x - bullet.position.x
        dy = asteroid.position.y - bullet.position.y
        distance = (dx**2 + dy**2)**0.5

        if distance < (asteroid.radius + bullet.radius):
          asteroid.split()
          bullet.kill()

      if playerChar.collides_with(asteroid):
        print("Game over!")
        import sys
        sys.exit()

    pygame.display.flip()
    
    # limit the framerate to 60 FPS
    dt= clock.tick(60)/ 1000


if __name__ == "__main__":
  main()
	
