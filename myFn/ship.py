import pygame
class Ship():

    def __init__(self,ai_settings,screen):
        #initialize spaceship and its location
        self.screen = screen
        self.ai_settings = ai_settings

        # load bmp image and get rectangle
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        #put spaceship on the bottom of window
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        Ship.center_ship(self)

    def blitme(self):
        #buld the spaceship at the specific location
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx

    def update(self):
        """Update the ship's position, based on movement flags."""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Update rect object from self.center.
        self.rect.centerx = self.center