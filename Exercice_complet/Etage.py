# -*-coding:UTF-8 -*
"""Classes pour GROUPE 6
"""

from Salle import Salle
from types import *

class Etage:
	"""Classe Etage
	"""

	def __init__(self, numero, surface, etages, affectation):
		
		assert type(numero) is IntType , "numero doit être un entier!" 
		assert type(surface) is IntType , "surface doit être un entier!" 

		# Assertion principle : we write what we want to have, here, a positive surface value.
		assert surface > 0 , "La surface ne peut être négative!" 

		if etages is not None:
			if len(etages) != 0:
				for etage in etages:
					assert etage.numero != numero, "Identifiant d'étage déjà existant!" 
				self.__numero = numero
		else :
			self.__numero = numero


		self.__surface = surface

		self.__affectation = affectation

		self.__salles = []


	def __getNumero(self):
		return self.__numero
	numero = property(__getNumero)

	def __getSurface(self):
		return self.__surface
	surface = property(__getSurface)


	def findSalle(self, num_salle):
		for salle in self.__salles:
			if salle.numero == num_salle:
				return salle
		return None

	def addSalle(self,num_salle, destination):
		if (len(self.__salles) > 0):
			self.__salles.append(Salle(num_salle,self.__salles, destination))
		else:
			self.__salles.append(Salle(num_salle,None, destination))

	def removeSalle(self, num_salle):
		for salle in self.__salles:
			if salle.numero == num_salle:
				self.__salles.remove(salle)
				return True
			else:
				return False

	def emptySalles(self):
		self.__salles = []

	def surfaceSalleMoyenne(self):
		if len(self.__salles) > 0:
			return self.__surface/(len(self.__salles)*1.0) # Multiply by 1.0 to force floating point division
		else:
			return 0.
