import sys
import pygame
from bullet import Bullet

def check_keydown_event(event, ai_settings, screen, ship, bullets):
    """Responde a pressionar de teclas"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Cria novo tiro
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_event(event, ship):
    """Responde a soltar de teclas"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """Responde a eventos de teclado e mouse"""
    # Monitora eventos de mouse e teclado
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)

def update_screen(ai_settings, screen, ship, bullets):
    """Atualiza imagens na tela e flip"""
    screen.fill(ai_settings.bg_color)
    
    # Redesenha tiros atras da nave e aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

    

    # Torna última tela desenhada visível
    pygame.display.flip()