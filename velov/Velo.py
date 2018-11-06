# -*-coding:UTF-8 -*
"""Classe pour les vélos
"""


class Velo:
	"""Classe Vélo
	"""
	
	def __init__(self, numero):
		self.__numero = numero

	def __get_numero(self):
		return self.__numero
	numero = property(__get_numero)

		
		
		
		
		