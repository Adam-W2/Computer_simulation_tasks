# Main file for Mars and Phobos simulation

import os
import sys
import numpy as np

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"   # suppress pygame msg
import pygame
from pygame.locals import QUIT, RLEACCEL
from Planet import Planet

# constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 720
NAME = "Mars and Phobos Simulator"

PHOBOS_SPRITE = "assets/phobos.jpg"
MARS_SPRITE = "assets/mars.jpg"

# sprites
class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, width, height):
        super(Sprite, self).__init__()  # this is a subclass of the sprite class
        sprite = pygame.image.load(image).convert_alpha()   # load image in, and convert the alpha (transparency)
        self.surf = pygame.transform.scale(sprite, (width, height))    # self.surf is like a texture we can use to render
        self.surf.set_colorkey((0, 0, 0), RLEACCEL) # set black colour to transparent
        self.rect = self.surf.get_rect(
            center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))   # self.rect goes alongside self.surf

class Main():
    # for updating velocity and coordinates of planets
    def update(r1, r2, mars, phobos, TIMESTEP):
        G = 6.67e-11
        
        # mars pos - phobos pos
        d1 = mars.get_coords() - phobos.get_coords()

        # acceleration of mars
        mars.set_acceleration(-(G * phobos.get_mass() * d1) / np.linalg.norm(d1)**3)

        # phobos pos - mars pos
        d2 = phobos.get_coords() - mars.get_coords()

        # acceleration of phobos
        mars.set_acceleration(-(G * mars.get_mass() * d2) / np.linalg.norm(d2)**3)

        # v = v + a * timestep
        temp = mars.get_velocity()
        mars.set_velocity(temp + mars.get_acceleration() * TIMESTEP)

        temp = phobos.get_velocity()
        phobos.set_velocity(temp + phobos.get_acceleration() * TIMESTEP)

        # coord system
        mars.set_coords(r1 + (mars.get_velocity() * TIMESTEP))
        phobos.set_coords(r2 + (phobos.get_velocity() * TIMESTEP))

    # actually render sprites and stuff
    def render(screen, mars, phobos, mars_sprite, phobos_sprite, font):
        # fill the background
        screen.fill((0, 0, 0))
        
        # render sprites
        screen.blit(mars_sprite.surf, mars_sprite.rect)
        screen.blit(phobos_sprite.surf, phobos_sprite.rect)
        
        # render text
        text_mars = font.render("Mars XY:" + str(mars.get_coords()) + " V:" + str(mars.get_velocity()), True, (255, 255, 255))
        text_phobos = font.render("Phobos XY:" + str(phobos.get_coords()) + " V:" + str(phobos.get_velocity()), True, (255, 255, 255))
        screen.blit(text_mars, (20, 24))
        screen.blit(text_phobos, (20, 50))

        # render the frame we just set up    
        pygame.display.flip()
    
    def main(self):
        running = True  # Important Boolean to keep program alive
        pygame.init()   # Pygame setup
        
        # Font setup
        pygame.font.init()
        font = pygame.font.SysFont("Mono", 16)

        # Create a window
        pygame.display.set_caption(NAME)    # Set window title
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        # instantiate sprite objects
        phobos_sprite = Sprite(PHOBOS_SPRITE, 24, 24)
        mars_sprite = Sprite(MARS_SPRITE, 64, 64)

        # initial maths setup
        r1 = np.array((0, 0))  # mars
        a1 = np.array((0, 0))
        mars = Planet("Mars", 6.4185e23, r1, np.array((0, 0)), a1)

        r2 = np.array((9.3773e6, 0))    # orbital radius of phobos
        a2 = np.array((0, 0))
        v_mag = (6.67e-11 * mars.get_mass() / np.linalg.norm(r2 - mars.get_coords()))**(1/2)    # calculated field
        phobos = Planet("Phobos", 1.06e16, r2, np.array((0, v_mag)), a2)
        
        TIMESTEP = 100    # How much stuff moves per update

        # main loop
        while (running):
            clock = pygame.time.Clock()
            clock.tick(60)  # fps setting

            # - render relative to middle of screen
            # - take away half of the w/h of sprite
            # - divide coords for scaling
            
            # update phobos sprite positi
            phobos_sprite.rect.left = (SCREEN_WIDTH / 2) - (phobos_sprite.rect.width / 2) - phobos.get_coords()[0] / 10
            phobos_sprite.rect.top = (SCREEN_HEIGHT / 2) - (phobos_sprite.rect.height / 2) - phobos.get_coords()[1] / 10

            # update mars sprite positio
            mars_sprite.rect.left = (SCREEN_WIDTH / 2) - (mars_sprite.rect.width / 2) - mars.get_coords()[0] / 1000000
            mars_sprite.rect.top = (SCREEN_HEIGHT / 2) - (mars_sprite.rect.width / 2) - mars.get_coords()[1] / 1000000
            
            # update our planet objects
            Main.update(r1, r2, mars, phobos, TIMESTEP)

            # debug statements
            #os.system('cls' if os.name == "nt" else "clear")
            #print(phobos)
            #print(mars)

            # call render func
            Main.render(screen, mars, phobos, mars_sprite, phobos_sprite, font)

            # check if we want to quit (alt f4, window close button etc)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == QUIT:
                    running = False

        # windows sucks so u gotta add these
        pygame.display.quit()
        pygame.quit()
        sys.exit()

# industry standard code to ensure code is only run if it's meant to be run
if __name__ == "__main__":
    Main.main()
