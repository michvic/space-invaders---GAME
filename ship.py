import pygame

class Ship():

    def __init__(self, scrren):
        """Inicializa a espaçonave e define sua posição inicial"""
        self.screen = scrren
 
        # Carrega a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load('images/millennium_falcon.bmp')
        self.rect = self.image.get_rect()
        self.screen_ret = scrren.get_rect()

        # Inicia cada nova espaçonave na parte inferior central da tela
        self.rect.centerx = self.screen_ret.centerx
        self.rect.bottom = self.screen_ret.bottom

        # Flag de movimento
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1
    def blitme(self):
        """Desenha a espaçonave em sua posição inical"""
        self.screen.blit(self.image, self.rect)
