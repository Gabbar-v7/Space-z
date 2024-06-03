import pygame

FPS = 60


def start(window, background):
    global FPS

    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        background.update()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

    return True
