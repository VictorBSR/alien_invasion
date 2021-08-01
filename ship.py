import pygame

class Ship():

    def __init__(self, screen):
        """Inicializa nave e pos inicial"""
        self.screen = screen

        # Carrega img da nave e rect
        self.image = pygame.image.load('images/ship2.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Inicializa nova nave
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Flag de movimento da nave
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """ Desenha a nave na pos atual """
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Atualiza posição da nave com base na flag de movimento"""
        if self.moving_right:
            self.rect.centerx += 1
        elif self.moving_left:
            self.rect.centerx -= 1