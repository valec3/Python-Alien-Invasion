import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen

        # Cargar la imagen del alien y establecer sus atributos rectangulares.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect() #obtener valores rectangulares

        # Comenzar cada nuevo alien cerca de la parte superior izquierda de la pantalla
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Almacenar las posiciones exactas horizontales de los aliens.
        self.x = float(self.rect.x)