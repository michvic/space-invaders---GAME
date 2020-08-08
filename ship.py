import pygame

class Ship():

    def __init__(self, ai_settings, scrren):
        """Inicializa a espaçonave e define sua posição inicial"""
        self.screen = scrren
        self.ai_settings = ai_settings
 
        # Carrega a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load('images/millennium_falcon.bmp')
        self.rect = self.image.get_rect()
        self.screen_ret = scrren.get_rect()



        # Inicia cada nova espaçonave na parte inferior central da tela
        self.rect.centerx = self.screen_ret.centerx
        self.rect.bottom = self.screen_ret.bottom - 5

        # Armazena um valor decimal para o centro da espaçonave
        self.center = float(self.rect.centerx)
        # Flag de movimento
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Atualizar a posição da espaçonave de acordo com as flags de movimentos"""
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        """Desenha a espaçonave em sua posição inical"""
        self.screen.blit(self.image, self.rect)
