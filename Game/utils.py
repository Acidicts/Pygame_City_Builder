import pygame

def draw_text(win, text, size, color, pos):

    font = pygame.font.Font(pygame.font.get_default_font(), size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(topleft=pos)

    win.blit(text_surface, text_rect)
