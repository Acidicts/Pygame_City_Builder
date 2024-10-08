import pygame as pg
import sys
from .world import World
from .settings import TILE_SIZE
from .utils import draw_text
from .camera import Camera
from .hud import Hud
from .resource_manager import ResourceManager
from .workers import Worker


class Game:

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()
        self.playing = False

        self.entities = []

        self.resource_manager = ResourceManager()

        self.hud = Hud(self.resource_manager, self.width, self.height)

        self.world = World(self.resource_manager, self.entities, self.hud, 50, 50, self.width, self.height)
        for _ in range(10):
            Worker(self.world.world[25][25], self.world)

        self.camera = Camera(self.width, self.height)

    def run(self):

        self.playing = True

        while self.playing:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()

    @staticmethod
    def events():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()

    def update(self):
        self.camera.update()

        for e in self.entities:
            e.update()

        self.hud.update()
        self.world.update(self.camera)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.world.draw(self.screen, self.camera)
        self.hud.draw(self.screen)

        draw_text(
            self.screen,
            'FPS : {}'.format(round(self.clock.get_fps())),
            20,
            (255, 255, 255),
            (5, 5)
        )

        pg.display.flip()
