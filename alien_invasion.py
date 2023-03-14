import sys 
import pygame
from studs import Settings
from ship import Ship
from blet import Bullet
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
        self.bullets = pygame.sprite.Group()
        
    def run_game(self):
        """Comenzar el bucle principal para el juego"""
        while True:
            self._check_events()#revisa los eventos
            self.ship.update()#actualiza la posicion de la nave
            self._update_bullets()#actualiza la posicion de las balas
            self._update_screen()#dibujasmos una nueva pantalla con las posiciones actuales
            self.clock.tick(60)
            
    def _check_events(self):
        """Reponde a las teclas presionadas y eventos del mouse"""
        #Ver eventos del teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type==pygame.KEYUP:
                self._check_keyup_events(event)
                    
    def _check_keydown_events(self, event):
            if event.key == pygame.K_RIGHT:
                #mover la nave a la derecha
                self.ship.moving_right=True
            elif event.key == pygame.K_LEFT:
                #mover la nave a la izquierda
                self.ship.moving_left=True
            elif event.key ==pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_SPACE:
                self._fire_bullet()
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            #mover la nave a la derecha
                self.ship.moving_right=False
        elif event.key == pygame.K_LEFT:
            #mover la nave a la izquierda
            self.ship.moving_left =False
    
    def _fire_bullet(self):
        """Crear una nueva bala y añadirla al grupo de balas."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
        
    
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()
        
        #Obtener rid de las balas que han pasado el limite
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
    
    def _update_screen(self):
        """Actualizar imagenes en la pantalla, y voltear a la nueva."""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()#dibujar nave
        pygame.display.flip()

if __name__ =="__main__":
    #Hacer una instancia, y correr el juego
    ai=AlienInvasion()
    ai.run_game()