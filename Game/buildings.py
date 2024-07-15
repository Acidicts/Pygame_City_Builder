import pygame

class Lumbermill:
    def __init__(self, pos, resource_manager):
        self.image = pygame.image.load("assets/graphics/building01.png")
        self.name = "lumbermill"
        self.rect = self.image.get_rect(topleft=pos)

        self.resource_manager = resource_manager
        self.resource_manager.apply_cost(self.name)

        self.resource_cooldown = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.resource_cooldown > 2000:
            self.resource_manager.resources["wood"] += 1
            self.resource_cooldown = now

class Stonemasonry:
    def __init__(self, pos, resource_manager):
        self.image = pygame.image.load("assets/graphics/building02.png")
        self.name = "stonemasonry"
        self.rect = self.image.get_rect(topleft=pos)

        self.resource_manager = resource_manager
        self.resource_manager.apply_cost(self.name)

        self.resource_cooldown = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.resource_cooldown > 2000:
            self.resource_manager.resources["stone"] += 1
            self.resource_cooldown = now
