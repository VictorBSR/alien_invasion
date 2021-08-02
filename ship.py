import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """Inicializa nave e pos inicial"""
        self.screen = screen
        self.ai_settings = ai_settings

        # Carrega img da nave e rect
        self.image = pygame.image.load('images/ship2.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Inicializa nova nave
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Armazena valor decimal para o centro da nave
        self.center = float(self.rect.centerx)

        # Flag de movimento da nave
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """ Desenha a nave na pos atual """
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Atualiza posição da nave com base na flag de movimento"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Atualiza rect
        self.rect.centerx = self.center