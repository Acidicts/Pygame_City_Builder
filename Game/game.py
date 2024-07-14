import pygame
import sys
from .world import World
from .settings import TILESIZE



class Game:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()
        self.playing = False

        self.world = World(10, 10, self.width, self.height)

    def run(self):
        self.playing = True

        while self.playing:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.playing = False
                    pygame.quit()
                    sys.exit()

    def update(self):
        pass

    def draw(self):
        self.screen.fill((0, 0, 0))

        for x in range(self.world.grid_length_x):
            for y in range(self.world.grid_length_y):

                sq = self.world.world[x][y]['cart_rect']
                rect = pygame.Rect(sq[0][0], sq[0][1], TILESIZE, TILESIZE)
                pygame.draw.rect(self.screen, (0, 0, 255), rect, 1)

                p = self.world.world[x][y]['iso_poly']
                p = [(x + self.width/2, y + self.height/4) for x, y in p]
                pygame.draw.polygon(self.screen, (255, 0, 0), p, 1)

        pygame.display.flip()
