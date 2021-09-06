from game_functions import check_events
import pygame #python -m pip install pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
    # Inicia jogo, configs e cria objeto tela
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Faz botão Play
    play_button = Button(ai_settings, screen, "Play")

    # Cria uma nova instância para armazenar estatísticas de jogo
    stats = GameStats(ai_settings)

    # Cria nave, grupo para tiros e grupo para aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Cria frota de aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start main loop
    while True:
        # Monitora eventos de mouse e teclado
        gf.check_events(ai_settings, screen, stats, play_button, ship, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)

run_game()