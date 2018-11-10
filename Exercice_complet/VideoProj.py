# -*-coding:UTF-8 -*
"""Classes pour GROUPE 6
"""

from types import * 


class VideoProj:
	"""Classe VideoProj
	"""
	
	def __init__(self, num_videoproj, nom_modele, luminosite, duree_ampoule, videoprojs):
		
		# Assertion principle : we write what we want to have, here, a positive surface value.
		assert type(num_videoproj) is IntType , "num_videoproj doit être un entier!" 
		assert type(nom_modele) is StringType , "nom_modele doit être une chaine de caractères!" 
		assert type(luminosite) is IntType , "luminosite doit être un entier!" 
		assert type(duree_ampoule) is IntType , "duree_ampoule doit être un entier!"
		
		
		if videoprojs is not None:
			if len(videoprojs) != 0:
				for numeroVideoproj in videoprojs.numero:
					assert numeroVideoproj != num_videoproj, "Identifiant de video projecteur déjà existant!" 
				self.__numero = num_videoproj
		else :
			self.__numero = num_videoproj


		self.__nom_modele = nom_modele

		self.__luminosite = luminosite

		self.__duree_ampoule = duree_ampoule
		
	def __getNumero(self):
		return self.__numero
	numero = property(__getNumero)		

		
	def __getNomModele(self):
		return self.__nom_modele
	nom_modele = property(__getNomModele)
	
	
	def __getLuminosite(self):
		return self.__luminosite
	luminosite = property(__getLuminosite)
	
	def __getDureeAmpoule(self):
		return self.__duree_ampoule
	duree_ampoule = property(__getDureeAmpoule)
	
	
	
