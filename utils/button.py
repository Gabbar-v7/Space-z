from typing import Callable

import pygame


class Button:
    def __init__(self,  surface: pygame.surface.Surface, image: pygame.surface.Surface, alpha: int, hover_alpha: int, center: tuple, onPress: callable) -> None:
        self.surface = surface

        self.image = image.copy()
        self.image.set_alpha(alpha)
        self.image_hover = image.copy()
        self.image_hover.set_alpha(hover_alpha)
        self.rect = image.get_rect()
        self.rect.center = center
        self.center = self.image.get_rect(center=center)

        self.onPress = onPress

    def pressed(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def place(self, mouse_pos: tuple = (-1, -1)):
        if not self.rect.collidepoint(mouse_pos):
            self.surface.blit(self.image, self.center)
        else:
            self.surface.blit(self.image_hover, self.center)
