from os.path import join

import pygame


class ImageScroll(pygame.sprite.Sprite):
    def __init__(self, window: pygame.surface.Surface, image_path: str,   width: float, height: float, alpha: int, start: float, end: float, speed: float, tiles: int):
        self.window = window

        image = pygame.image.load(image_path).convert_alpha()
        image.set_alpha(alpha)
        self.image = pygame.transform.scale(image, (width, height))

        self.height = height
        self.start = start
        self.end = end
        self.speed = speed
        self.tiles = tiles

    def update(self):
        for i in range(0, self.tiles):
            self.window.blit(
                self.image, (0, i * self.height * -1 + self.start))

        # scroll background
        self.start += self.speed

        # reset scroll
        if self.start > self.end:
            self.start = 0
