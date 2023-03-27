import pygame

class Ship:
    """Una clase para manejar la nave."""
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings=ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        
        #Almacenar un flotante para la posicion horizontal exacta de la nave
        self.x=float(self.rect.x)
        
        #Movimiento bandera
        self.moving_right=False
        self.moving_left=False
        
    def update(self):
        """Actualizar la posicion de la nave basado en la bandera"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -=self.settings.ship_speed
        #Actualizar rect objeto de self.x
        self.rect.x=self.x
        
    def blitme(self):
        """Dibuja la nave en la posicion especificada"""
        self.screen.blit(self.image, self.rect)
        
    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)