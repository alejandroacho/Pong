import pygame
from settings import *

def initialize_game():
    pygame.init()

def get_initial_items():
    screen = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()
    return screen, clock

def should_quit(event):
    if event.type == pygame.QUIT:
        return True
    return False

def draw_elements(screen, player1, player2, ball):
    screen.fill(BLACK)
    player_1 = player1.draw(screen)
    player_2 = player2.draw(screen)
    ball_draw = ball.draw(screen)
    return player_1, player_2, ball_draw

def refresh_screen(clock):
    pygame.display.flip()
    clock.tick(60)

def quit_game():
    pygame.quit()