import pygame
from .settings import TILESIZE


class World:
    def __init__(self, grid_length_x, grid_length_y, width, height):
        self.grid_length_x = grid_length_x
        self.grid_length_y = grid_length_y
        self.width = width
        self.height = height

        self.world = self.create_world()

    def create_world(self):

        world = []

        for grid_x in range(self.grid_length_x):
            world.append([])
            for grid_y in range(self.grid_length_y):
                world_tile = self.grid_to_world(grid_x, grid_y)
                world[grid_x].append(world_tile)

        return world

    def grid_to_world(self, grid_x, grid_y):
        rect = [
            (grid_x * TILESIZE, grid_y*TILESIZE),
            (grid_x * TILESIZE + TILESIZE, grid_y*TILESIZE),
            (grid_x * TILESIZE + TILESIZE, grid_y*TILESIZE + TILESIZE),
            (grid_x * TILESIZE, grid_y*TILESIZE + TILESIZE)
        ]

        iso_poly = [self.cart_to_iso(x, y) for x, y in rect]

        out = {
            "grid": [grid_x, grid_y],
            "cart_rect": rect,
            'iso_poly': iso_poly,
        }

        return out

    def cart_to_iso(self, x, y):
        iso_x = x - y
        iso_y = (x + y) / 2

        return iso_x, iso_y
