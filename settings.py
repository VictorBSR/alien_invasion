class Settings():
    """Classe para armazenar todas as configurações para Alien Invasion"""

    def __init__(self):
        """Inicializa as configs do jogo"""
        # Configs de tela
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (59, 30, 128)

        # Configs de nave
        self.ship_speed_factor = 1.5

        # Configs de tiro
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 230, 160, 6