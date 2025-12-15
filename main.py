from textwrap import fill

import pygame
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from logger import log_state
from player import Player


def main():
    print("Starting Asteroids with pygame version: VERSION")

    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.time.Clock()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    dt = 0
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
        fps =pygame.time.Clock().tick(60)
        dt = fps/1000


if __name__ == "__main__":
    main()
