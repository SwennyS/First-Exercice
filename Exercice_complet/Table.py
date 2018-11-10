# -*-coding:UTF-8 -*
"""Classes pour GROUPE 6
"""
from types import *

class Table:
	"""Classe Table
	"""
	
	def __init__(self, num_table, largeur, longueur, tables):
		
		# Assertion principle : we write what we want to have, here, a positive surface value.
		assert type(num_table) is IntType , "num_table doit être un entier!" 
		assert type(largeur) is IntType , "largeur doit être un entier!" 
		assert type(longueur) is IntType , "longueur doit être un entier!" 
		
		
		if tables is not None:
			if len(tables) != 0:
				for numeroTable in tables.numero:
					assert numeroTable != num_table, "Identifiant de table déjà existant!" 
				self.__numero = num_table
		else :
			self.__numero = num_table

		self.__largeur = largeur

		self.__longueur = longueur
		
	def __getNumero(self):
		return self.__numero
	numero = property(__getNumero)
		
		
	def __getLargeur(self):
		return self.__largeur
	largeur = property(__getLargeur)

		
	def __getLongueur(self):
		return self.__longueur
	longueur = property(__getLongueur)
	
	

	
	
