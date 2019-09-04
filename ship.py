import pygame

class Ship():

    def __init__(self, scrren):
        """Inicializa a espaçonave e define sua posição inicial"""
        self.screen = scrren

        # Carrega a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load('images/ship.py.bmp')
        self.rect = self.image.get_rect()
        self.screen_ret = scrren.get_rect()

        # Inicia cada nova espaçonave na parte inferior central da tela
        self.rect.centerx = self.screen_ret.centerx
        self.rect.bottom = self.screen_ret.bottom

    def blitme(self):
        """Desenha a espaçonave em sua posição inical"""
        self.screen.blit(self.image, self.rect)
