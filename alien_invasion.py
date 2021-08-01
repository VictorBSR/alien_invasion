from game_functions import check_events
import pygame #python -m pip install pygame
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
    ship = Ship(screen)

    # Start main loop
    while True:

        # Monitora eventos de mouse e teclado
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

run_game()