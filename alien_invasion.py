import sys
import pygame

def run_game():
    # Inicia jogo e cria objeto tela
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")