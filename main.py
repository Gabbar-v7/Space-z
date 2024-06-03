from os import environ
from os.path import join

import pygame

from utils.button import Button
from utils.image_scroll import ImageScroll
from utils.start_page import start

# Initializtion
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 480, 720
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BTN_START = 140
BTN_GAP = 50
FONTS = {'game_race_30': pygame.font.Font(join('assets', 'fonts', 'Hard Race.otf'), 30),
         'game_race_48': pygame.font.Font(join('assets', 'fonts', 'Hard Race.otf'), 48),
         }

# Window Settings
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
icon = pygame.image.load(join('assets', 'icons', 'icon.png'))
pygame.display.set_icon(icon)
pygame.display.set_caption("Space-Z")
window.fill(BLACK)
# Elements
stars_bg = ImageScroll(window,
                       join('assets', 'backgrounds', 'stars.jpg'), SCREEN_WIDTH, SCREEN_HEIGHT, alpha=255, start=0, end=SCREEN_HEIGHT, speed=.3, tiles=2)

head_label = FONTS['game_race_48'].render('Trax Inc.', True, WHITE)
head_label = head_label, head_label.get_rect(
    center=(SCREEN_WIDTH/2, 110))

start_btn = Button(window, FONTS['game_race_30'].render('Start', True, WHITE), 178, 255,
                   (SCREEN_WIDTH/2, (SCREEN_HEIGHT/2)+BTN_START), lambda: start(window, stars_bg))
highscrore_btn = Button(window, FONTS['game_race_30'].render('Highscore', True, WHITE), 178, 255,
                        (SCREEN_WIDTH/2, (SCREEN_HEIGHT/2)+BTN_START+BTN_GAP), lambda: print('highscore'))
setting_btn = Button(window, FONTS['game_race_30'].render('Settings', True, WHITE), 178, 255,
                     (SCREEN_WIDTH/2, (SCREEN_HEIGHT/2)+BTN_START+BTN_GAP*2), lambda: print('setting'))
info_btn = Button(window, pygame.image.load(join('assets', 'icons', 'info.png')).convert_alpha(), 178, 255,
                  (SCREEN_WIDTH-30, SCREEN_HEIGHT-30), lambda: print('setting'))


def main():
    # Loop settings
    clock = pygame.time.Clock()
    run = True

    # Variables
    global window, stars_bg, start_btn, highscrore_btn, setting_btn, info_btn

    while run:
        # Game update
        clock.tick(FPS)

        mouse_pos = pygame.mouse.get_pos()

        # Elements
        stars_bg.update()
        window.blit(*head_label)
        start_btn.place(mouse_pos)
        highscrore_btn.place(mouse_pos)
        setting_btn.place(mouse_pos)
        info_btn.place(mouse_pos)
        pygame.display.update()

        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == 13:  # Press Enter
                    run = start_btn.onPress()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_btn.pressed():
                    run = start_btn.onPress()
                elif highscrore_btn.pressed():
                    highscrore_btn.onPress()
                elif setting_btn.pressed():
                    setting_btn.onPress()
                elif info_btn.pressed():
                    info_btn.onPress()
            elif event.type == pygame.QUIT:
                run = False


if __name__ == '__main__':
    main()
    pygame.quit()
