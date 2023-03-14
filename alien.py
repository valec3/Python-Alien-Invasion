import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        # Cargar la imagen del alien y establecer sus atributos rectangulares.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect() #obtener valores rectangulares

        # Comenzar cada nuevo alien cerca de la parte superior izquierda de la pantalla
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Almacenar las posiciones exactas horizontales de los aliens.
        self.x = float(self.rect.x)
    
    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
    
    def update(self):
        """Move the alien to the right."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x