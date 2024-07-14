import pygame
from Game.game import Game


def main():

    running = True
    playing = True

    pygame.init()
    pygame.mixer.init()
    win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    clock = pygame.time.Clock()

    # Menus


    # Game
    game = Game(win, clock)

    while running:

        while playing:
            game.run()


if __name__ == "__main__":
    main()
