class GameStats():
    '''Verifica estatísticas do Alien Invasion'''

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        # Nunca resetar high score
        self.high_score = 0

    def reset_stats(self):
        # Verifica número de naves restantes
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1