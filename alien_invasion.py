import sys 

import pygame
from studs import Settings
from ship import Ship
class AlienInvasion:
    """Clase general para gestionar los activos y el comportamiento del juego."""
    def __init__(self):
        """Inicializar el juego, y crear los recursos"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings=Settings()
        self.screen=pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        self.ship =Ship(self)
        
    def run_game(self):
        """Comenzar el bucle principal para el juego"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)
            
    def _check_events(self):
        """Reponde a las teclas presionadas y eventos del mouse"""
        #Ver eventos del teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #mover la nave a la derecha
                    self.ship.moving_right=True
                elif event.key == pygame.K_LEFT:
                    #mover la nave a la izquierda
                    self.ship.moving_left=True
                    
            elif event.type==pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    #mover la nave a la derecha
                    self.ship.moving_right=False
                elif event.key == pygame.K_LEFT:
                    #mover la nave a la izquierda
                    self.ship.moving_left =False
                    
    def _update_screen(self):
        """Actualizar imagenes en la pantalla, y voltear a la nueva."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

if __name__ =="__main__":
    #Hacer una instancia, y correr el juego
    ai=AlienInvasion()
    ai.run_game()