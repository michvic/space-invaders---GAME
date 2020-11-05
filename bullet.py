import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
  """ Uma classe que administra projéteis disparados pela espaçonave """

  def __init__(self, ai_settings, screen, ship):
    super().__init__()
    self.screen = screen

    # cria um retângulo para o projétil em (0,0) e, em seguida define a posição correta
    self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
    self.rect.centerx = ship.rect.centerx
    self.rect.top = ship.rect.top

    # armazena a posiçao do projétil com valor decimal
    self.y = float(self.rect.y)

    self.color = ai_settings.bullet_color
    self.speed_factor = ai_settings.bullet_speed_factor

  def update(self):
    """ move o projétil para cima da tela """
    self.y -= self.speed_factor
    self.rect.y = self.y
  
  def draw_bullet(self):
    pygame.draw.rect(self.screen, self.color, self.rect)