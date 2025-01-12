import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    updatable = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawables)
    AsteroidField.containers = updatable
    Player.containers = (updatable, drawables)
    player = Player(x,y)
    asteroidfield = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.fill(0)
        updatable.update(dt)
        for sprite in drawables:
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()