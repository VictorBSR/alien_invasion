import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Gerencia os tiros da nave"""

    def __init__(self, ai_settings, screen, ship):
        """Inicializa tiro e pos inicial (mesma da nave)"""
        super().__init__()
        self.screen = screen

        # Cria rect do tiro no (0,0) e corrige posição
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Armazena valor decimal para o centro da nave
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move o tiro para cima"""
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """Desenha o tiro"""
        pygame.draw.rect(self.screen, self.color, self.rect)