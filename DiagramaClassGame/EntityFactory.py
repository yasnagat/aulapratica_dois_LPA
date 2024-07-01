#!/usr/bin/python
#-*- coding: utf-8 -*-

from Background import Background

class EntityFactory(Background):
	def __init__(self):
		pass

	def get_entity(self, entityt_type):
		"""
		o get_entity é o único método necessário e que vai ser chamado.
		lembre que o level precisar gerar um novo player, enemy ou background, é só chamar a fábrica
		"""
		pass

