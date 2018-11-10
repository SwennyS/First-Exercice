# -*-coding:UTF-8 -*
"""Classes pour GROUPE 6
"""
from types import *


class Siege:
	"""Classe Siege
	"""
	
	def __init__(self, num_siege, type_siege ,sieges):
		
		# Assertion principle : we write what we want to have, here, a positive surface value.
		assert type(num_siege) is IntType , "num_siege doit être un entier!" 
		
		if sieges is not None:
			if len(sieges) != 0:
				for numeroSiege in sieges.numero:
					assert numeroSiege != num_siege, "Identifiant de siege déjà existant!" 
				self.__numero = num_siege
		else :
			self.__numero = num_siege
			
			self.__type_siege = type_siege
			
						
	def __getNumero(self):
		return self.__numero
	numero = property(__getNumero)


	def __getTypeSiege(self):
		return self.__type_siege
	type_siege = property(__getTypeSiege)
	

