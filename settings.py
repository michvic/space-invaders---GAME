class Settings():
    """ Uma classe para armazena todas as configuraç�es da Invassao Alienigena. """

    def __init__(self):
        """ Inicializa as configuraçoes do jogo. """
        # Configuraçao da tela
        self.screen_width = 1200
        self.screen_height = 800
        # self.bg_color = (230, 230, 230)
        self.bg_color = (0,0,0)

        # Configurações espaçonave
        self.ship_speed_factor = 1.5

        # Configuração dos projéteis
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 121, 232, 232
        