import pygame
from random import randint as randomNumber

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)

pygame.init()

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Bouncing Ball Game")

clock = pygame.time.Clock()

class Particle:

  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.v_x = randomNumber(-20, 20)
    self.v_y = randomNumber(-20, 20)
    self.color = (randomNumber(0, 255), randomNumber(0, 255), randomNumber(0, 255))

  def step(self):
    self.draw()
    self.move()
    self.handleBounce()

  def draw(self):
    pygame.draw.circle(screen, self.color, (self.x, self.y), 30, 0)

  def move(self):
    self.x += self.v_x
    self.y += self.v_y

  def handleBounce(self):
    if self.x < 0 or self.x > SCREEN_WIDTH:
      self.v_x *= -1
    if self.y < 0 or self.y > SCREEN_HEIGHT:
      self.v_y *= -1

particles = []

# -------- Main Program Loop -----------
done = False
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONUP:
          x, y = pygame.mouse.get_pos()
          particle = Particle(x, y)
          particles.append(particle)

    screen.fill(GREEN)

    for particle in particles:
      particle.step()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
exit()
