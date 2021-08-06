import pygame
from settings import *

class Player():
    def __init__(self, player_number):
        self.player_number = player_number
        self.color = WHITE
        self.x = self.initial_x()
        self.y = self.initial_y()
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.dimensions = (self.width, self.height)
        self.speed = PLAYER_INITIAL_SPEED

    def initial_x(self):
        """
        This function returns the initial x position of the player.
        """
        is_player_one = self.player_number == 1
        player_initial_x_position = PLAYER_ONE_INITIAL_X if is_player_one\
                                    else PLAYER_TWO_INITIAL_X
        return player_initial_x_position
    
    def initial_y(self):
        """
        This function returns the initial y position of the player.
        """
        is_player_one = self.player_number == 1
        player_initial_x_position = PLAYER_ONE_INITIAL_Y if is_player_one\
                                    else PLAYER_TWO_INITIAL_Y
        return player_initial_x_position
    
    def movement(self, event):
        """
        This function updates the player's position based on the key pressed.
        """
        try:
            key_affected = event.key
            key_was_pressed = event.type == pygame.KEYDOWN
            key_was_unpressed = event.type == pygame.KEYUP
            if key_affected in PLAYERS_MOVEMENTS:
                if key_was_pressed:
                    self.move(key_affected)
                if key_was_unpressed:
                    self.stop(key_affected)
        except:
            pass

    def move(self, key_pressed):
        """
        This function moves players according to the key pressed.
        """       
        player_number = self.player_number
        is_player_one = player_number == 1
        is_player_two = player_number == 2

        if is_player_one and key_pressed in PLAYER_ONE_MOVEMENTS:
            move_up = key_pressed == PLAYER_ONE_UP_KEY
            self.speed = -PLAYER_SPEED if move_up else PLAYER_SPEED

        if is_player_two and key_pressed in PLAYER_TWO_MOVEMENTS:
            move_up = key_pressed == PLAYER_TWO_UP_KEY
            self.speed = -PLAYER_SPEED if move_up else PLAYER_SPEED

    def stop(self, key_unpressed):
        """
        This function stops players according to the key pressed.
        """
        player_number = self.player_number

        if player_number == 1:
            if key_unpressed in PLAYER_ONE_MOVEMENTS:
                self.speed = PLAYER_STOP

        if player_number == 2:
            if key_unpressed in PLAYER_TWO_MOVEMENTS:
                self.speed = PLAYER_STOP
    
    def update_position(self):
        """
        This function updates the position of the player.
        """
        is_on_top = self.y <= 1
        is_on_bottom = self.y >= 510
        is_moving_up = self.speed < 0
        is_moving_down = self.speed > 0

        if is_on_top and is_moving_down:
            self.y += self.speed
        
        if is_on_bottom and is_moving_up:
            self.y += self.speed
        
        if not is_on_top and not is_on_bottom:
            self.y += self.speed

        return self.y
    
    def draw(self, screen):
        """
        This function draws the player on the screen.
        """
        coordinates = (self.x, self.update_position())
        player_parameters = (coordinates + self.dimensions)
        player_draw_object = pygame.draw.rect(screen, WHITE, player_parameters)
        return player_draw_object

class Ball():
    def __init__(self):
        self.color = WHITE
        self.x = BALL_INITIAL_X
        self.y = BALL_INITIAL_Y
        self.speed_x = BALL_INITIAL_SPEED_X
        self.speed_y = BALL_INITIAL_SPEED_Y
        self.radius = BALL_RADIUS
    
    def movement(self):
        """
        This function moves the ball.
        """
        self.check_for_screen_collides()
        self.check_if_ball_quit_screen()
        self.update_position()

    def check_for_screen_collides(self):
        """"
        This function checks if the ball collides with the screen.
        """
        if self.y > 590 or self.y < 10:
            self.speed_y *= -BALL_SPEED
    
    def check_if_ball_quit_screen(self):
        """
        This function checks if the ball went out of the screen.
        """
        went_out_through_right_side = self.x > 800
        if went_out_through_right_side:
            self.ball_went_out_through_right_side()

        went_out_through_left_side = self.x < 0
        if went_out_through_left_side:
            self.ball_went_out_through_left_side()
    
    def ball_went_out_through_right_side(self):
        """
        This function updates the ball's position when it went
        out of the rigth side screen.
        """
        
        self.x = 400
        self.y = 300
        self.inver_direction()

    def ball_went_out_through_left_side(self):
        """
        This function updates the ball's position when it went
        out of the left side screen.
        """
        self.x = 400
        self.y = 300
        self.inver_direction()
    
    def inver_direction(self):
        """
        This function inverts the direction of the ball.
        """
        self.speed_x *= -BALL_SPEED
        self.speed_y *= -BALL_SPEED
    
    def update_position(self):
        """
        This function updates the position of the ball.
        """
        self.x += self.speed_x
        self.y += self.speed_y
    
    def draw(self, screen):
        """"
        This function draws the ball on the screen.
        """
        coordinates = (self.x, self.y)
        ball_draw_object = pygame.draw.circle(screen, WHITE, coordinates, self.radius)
        return ball_draw_object
        
    def update_position(self):
        """
        This function updates the ball coordinates.
        """
        self.x += self.speed_x
        self.y += self.speed_y
    
    def check_player_collide(self, player_1, player_2, ball):
        """
        This function checks if the ball collides with the players.
        """
        if ball.colliderect(player_1) or ball.colliderect(player_2):
            self.speed_x *= -1

