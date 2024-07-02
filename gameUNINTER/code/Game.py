#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Menu import Menu


class Game:
	"""
	Game é uma classe. A ela foi atribuída um ATRIBUTO chamado tela do tipo Surface e um MÉTODO (operation) chamado run, que é uma habilidade que terá no jogo. 
	Ela é a classe principal, a qual se ligam as outras (MENU e LEVEL), por meio de uma composição.
	"""
	def __init__(self):
		self.screen = None
		pygame.init()  # é uma boa prática dar o init com pygame
		self.Screen = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
		# alterar valores de constantes é bem difícil
		# por isso o ideal é criar um arquivo para conter todas as constantes, como os tamanhos das imagens
	def run(self):

		while True:
			menu = Menu(self.Screen)

			menu.run()  # o run é o método que permite que o objeto seja executado







