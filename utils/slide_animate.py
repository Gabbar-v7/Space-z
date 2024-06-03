import pygame


class Slide:
    def __init__(self, window: pygame.surface.Surface, widget, start, end, speed) -> None:
        self.window = window
        self.widget = widget
        self.current = start
        self.end = end
        self.speed = speed

    def replace(self):
        for i in range(0, self.tiles):
            self.window.blit(
                self.image, (0, i * self.height * -1 + self.start))

            # scroll background
            self.start += self.speed

            # reset scroll
            if self.current > self.end:
                return True
        return False
