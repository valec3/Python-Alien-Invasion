import sys 

import pygame

class AlienInvasion:
    """Clase general para gestionar los activos y el comportamiento del juego."""
    def __init__(self):
        """Inicializar el juego, y crear los recursos"""
        pygame.init()
        
        self.screen=pygame.display.set_model((1200,800))
        pygame.display.set_caption("Alien Invasion")
        
    def run_game(self):
        """Comenzar el bucle principal para el juego"""
        while True:
            #Ver eventos del teclado
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #Hacer visible la pantalla dibijada mas recientemente
            pygame.display.flip()

if __name__ =="__main__":
    #Hacer una instancia, y correr el juego
    ai=AlienInvasion()
    ai.run_game()