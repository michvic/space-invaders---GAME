import sys
import pygame
from settings import Settings

def run_game():
    # Inicializa o pygame, as configurações e cria um objeto screen
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Define a cor de fundo
    bg_color = (230, 230, 230)

    # Inicia o laço principal do jogo
    while True:

        # Observa os eventos do mouse e de teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redesenha a tela a cada passagem pelo laço
        screen.fill(ai_settings.bg_color)

        # Deixa a tela visivel
        pygame.display.flip()


run_game()