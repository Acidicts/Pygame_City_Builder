import pygame
from.utils import draw_text


class Hud:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.hud_color = (198, 155, 93, 175)

        self.resources_surface = pygame.Surface((self.width, self.height * 0.02), pygame.SRCALPHA)
        self.resources_surface.fill(self.hud_color)

        self.build_surface = pygame.Surface((self.width * 0.15, self.height * 0.25), pygame.SRCALPHA)
        self.build_surface.fill(self.hud_color)

        self.select_surface = pygame.Surface((self.width * 0.3, self.height * 0.2), pygame.SRCALPHA)
        self.select_surface.fill(self.hud_color)

        self.images = self.load_images()
        self.tiles = self.create_build_hud()

        self.selected_tile = None

    def create_build_hud(self):
        render_pos = [self.width * 0.84 + 10, self.height * 0.74 + 10]
        object_width = self.build_surface.get_width() // 5

        tiles = []

        for image_name, image in self.images.items():
            pos = render_pos.copy()
            image_tmp = image.copy()
            image_scale = self.scale_image(image_tmp, object_width, object_width)
            rect = image_scale.get_rect(topleft=pos)

            tiles.append(
                {
                    "name": image_name,
                    "icon": image_scale,
                    "image": image_scale,
                    "rect": rect
                }
            )

            render_pos[0] += image_scale.get_width() + 10

        return tiles

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_action = pygame.mouse.get_pressed()

        if mouse_action[2]:
            self.selected_tile = None

        for tile in self.tiles:
            if tile["rect"].collidepoint(mouse_pos):
                if mouse_action[0]:
                    self.selected_tile = tile
                break

    def draw(self, win):

        if self.selected_tile is not None:
            img = self.selected_tile["image"].copy()
            img.set_alpha(100)
            win.blit(img, pygame.mouse.get_pos())

        win.blit(self.resources_surface, (0, 0))

        win.blit(self.build_surface, (self.width * 0.84, self.height * 0.74))

        win.blit(self.select_surface, (self.width * 0.35, self.height * 0.79))

        for tile in self.tiles:
            win.blit(tile["icon"], tile["rect"].topleft)

        pos = self.width - 400
        for resource in ["Wood:", "Stone:", "Food:"]:
            draw_text(win, resource, 20, (255, 255, 255), (pos, 0))
            pos += 100

    @staticmethod
    def load_images():

        building1 = pygame.image.load("assets/graphics/building01.png")
        building2 = pygame.image.load("assets/graphics/building02.png")
        tree = pygame.image.load("assets/graphics/tree.png")
        rock = pygame.image.load("assets/graphics/rock.png")

        images = {
            "building1": building1,
            "building2": building2,
            "tree": tree,
            "rock": rock,
        }

        return images

    @staticmethod
    def scale_image(image, w=None, h=None):

        if w is None and h is None:
            pass
        elif h is None:
            scale = w / image.get_width()
            h = scale * image.get_height()
            image = pygame.transform.scale(image, (w, int(h)))
        elif w is None:
            scale = h / image.get_height()
            w = scale * image.get_width()
            image = pygame.transform.scale(image, (int(w), h))
        else:
            image = pygame.transform.scale(image, (w, h))

        return image
