import sys
import pygame

def run_game():
    # Inicializa o jogo e cria um objeto para a tela
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
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
        screen.fill(bg_color)

        # Deixa a tela visivel
        pygame.display.flip()


run_game()