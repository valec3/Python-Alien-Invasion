import sys 

import pygame
from studs import Settings
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
        # Establecer el color de fondo.
        self.bg_color = (230, 230, 230)
        
    def run_game(self):
        """Comenzar el bucle principal para el juego"""
        while True:
            #Ver eventos del teclado
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #Redibujar la pantalla durante cada paso del bucle
            self.screen.fill(self.settings.bg_color)
            #Hacer visible la pantalla dibijada mas recientemente
            pygame.display.flip()
            self.clock.tick(60)

if __name__ =="__main__":
    #Hacer una instancia, y correr el juego
    ai=AlienInvasion()
    ai.run_game()