import pygame

from settings import *
from models import *
from functions import *

initialize_game()

screen, clock = get_initial_items()
p1 = Player(1)
p2 = Player(2)
ball = Ball()
game_over = False

while not game_over:
    for event in pygame.event.get():
        game_over = should_quit(event)
        p1.movement(event)
        p2.movement(event)
    ball.movement()
    _p1, _p2, _ball = draw_elements(screen, p1, p2, ball)
    ball.check_player_collide( _p1, _p2, _ball)
    refresh_screen(clock)

quit_game()
