#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH


class Menu:
    """A classe MENU tem como"""

    def __init__(self, screen):
        self.screen: Surface = screen  # melhor declaraer para conseguir chamar lá embaixo
        self.surf = pygame.image.load('./asset/MenuBG.png')
        self.rect = self.surf.get_rect(left=0, top=0)  # o retângulo define como o código se relacionará com a imagem

    # é necessário sempre repetir o self junto, pois a variável é composta por ele
    # agora é necessário desenhar a imagem no código
    def run(self):
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.screen.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Mountain", (255, 128, 0), ((WIN_WIDTH / 2), 70))
            # é um método da própria classe lá debaixo
            pygame.display.flip()
        pass

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_position: tuple):
        text_font: Font = pygame.font.SysFont("Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_position)
        self.screen.blit(source=text_surf, dest=text_rect)
