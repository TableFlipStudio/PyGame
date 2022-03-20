import pygame
import sys

from save import Button

class MainMenu():
    """Menu główne, wczytywane przed uruchomieniem run_game()"""

    def __init__(self, dogex):
        self.settings = dogex.settings
        self.screen = dogex.screen
        self.screen_rect = dogex.screen_rect

        self.image = pygame.image.load("images/mainmenu.bmp")
        self.rect = self.image.get_rect()
        self.rect.topleft = self.screen_rect.topleft

        ngpos = (self.settings.screen_width / 5,
            self.settings.screen_height / 2.5)
        self.newgamebutton = Button(self, ngpos, "New game")

        lgpos = (ngpos[0], ngpos[1] + self.settings.button_space)
        self.loadgamebutton = Button(self, lgpos, "Load game")

        qpos = (lgpos[0], lgpos[1] + self.settings.button_space)
        self.quitbutton = Button(self, qpos, "Quit")

    def check_events(self, dogex):
        """Metoda identyczna jak _check_events() klasy DoGeX(), służy
        jednak ona do detekcji zdarzeń na etapie menu głównego, czyli przed
        uruchomieniem gry jako takiej."""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if self.newgamebutton.rect.collidepoint(mouse_pos):
                    dogex._reset_save()
                    return True

                elif self.loadgamebutton.rect.collidepoint(mouse_pos):
                    dogex._load_save()
                    return True

                elif self.quitbutton.rect.collidepoint(mouse_pos):
                    sys.exit()

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        self.newgamebutton.blit_button()
        self.loadgamebutton.blit_button()
        self.quitbutton.blit_button()
