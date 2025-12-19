import sys
import pygame
from asteroid import Asteroid
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from logger import log_event, log_state
from player import Player
from asteroidfield import AsteroidField


def main():
    print("Starting Asteroids with pygame version: VERSION")

    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    dt = 0

    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over")
                sys.exit()
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()
        fps = clock.tick(60)
        dt = fps / 1000


if __name__ == "__main__":
    main()
