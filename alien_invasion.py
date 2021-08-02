from game_functions import check_events
import pygame #python -m pip install pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Inicia jogo, configs e cria objeto tela
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Cria nave
    ship = Ship(ai_settings, screen)
    # Cria grupo para tiros
    bullets = Group()

    # Start main loop
    while True:
        # Monitora eventos de mouse e teclado
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        
        # Apaga balas fora da tela
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0: # topo da tela
                bullets.remove(bullet)
        print(len(bullets))

        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()