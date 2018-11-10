# -*-coding:UTF-8 -*
"""Classes pour GROUPE 6
"""

from types import *

class Cours:
	"""Classe Cours
	"""
	
	def __init__(self, id_cours, nom_cours, nb_seance, nb_heure, code_cours):
		
		# Assertion principle : we write what we want to have, here, a positive surface value.
		assert type(id_cours) is IntType , "id_cours doit être un entier!" 
		assert type(nom_cours) is StringType , "nom_cours doit être un entier!" 
		assert type(nb_seance) is IntType , "nb_seance doit être un entier!" 
		assert type(nb_heure) is IntType , "nb_heure doit être un entier!" 
				
		if courss is not None:
			if len(courss) != 0:
				for cours in courss:
					assert cours.id != id, "Identifiant d'étage déjà existant!" 
				self.__id = id
		else :
			self.__id = id


	def __getCodeCours(self):
		return self.__code_cours
	code_cours = property(__getCodeCours)
