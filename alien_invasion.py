import sys 
from time import sleep

import pygame
from studs import Settings
from game_stats import GameStats
from ship import Ship
from blet import Bullet
from alien import Alien

class AlienInvasion:
    """Clase general para gestionar los activos y el comportamiento del juego."""
    def __init__(self):
        """Inicializar el juego, y crear los recursos"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings=Settings()
        #Establecer el tamaño de la pantalla
        self.screen=pygame.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")
        # Create an instance to store game statistics.
        self.stats = GameStats(self)
        
        self.ship =Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        
        # Start Alien Invasion in an active state.
        self.game_active = True
        

    def run_game(self):
        """Comenzar el bucle principal para el juego"""
        while True:
            self._check_events()#revisa los eventos
            
            if self.game_active:
                self.ship.update()#actualiza la posicion de la nave
                self._update_bullets()#actualiza la posicion de las balas
                self._update_aliens() #Mover aliens
            
            self._update_screen()#dibujasmos una nueva pantalla con las posiciones actuales
            self.clock.tick(60)#Velocidad de fotogramas por segundo

    def _check_events(self):
        """Reponde a las teclas presionadas y eventos del mouse"""
        #Ver eventos del teclado
        for event in pygame.event.get():#recoge cada evento
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type==pygame.KEYUP:
                self._check_keyup_events(event)
                    

    def _check_keydown_events(self, event):
            """Detecta las teclas PRESIONADAS"""
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
        """Detecta las teclas SOLTADAS luego de ser presionadas"""
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
        # Check for any bullets that have hit aliens.
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Decrement ships_left.
            self.stats.ships_left -= 1
            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()
            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()
            # Pause.
            sleep(0.5)
        else:
            self.game_active=False

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break

    def _update_aliens(self):
        """Update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()
        # Mirar la colision entre nave-alien.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        
        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    def _create_fleet(self):
        """Crear la flota de aliens"""
        # Hacer un alien.
        # Create an alien and keep adding aliens until there's no room left.
        # Spacing between aliens is one alien width.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size #obtenemos el ancho y alto del 1er alien
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            # Finished a row; reset x value, and increment y value.
            current_x = alien_width
            current_y += 2 * alien_height
        
    def _create_alien(self, x_position, y_position):
        """Crear un alien y place it in the row."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)  
    
    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """Actualizar imagenes en la pantalla, y voltear a la nueva."""
        self.screen.fill(self.settings.bg_color)#color de fondo
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()#dibujar nave
        self.aliens.draw(self.screen) #dibujar alien
        pygame.display.flip()#hacer visible la pantalla mas actual

if __name__ =="__main__":
    #Hacer una instancia, y correr el juego
    ai=AlienInvasion()
    ai.run_game()