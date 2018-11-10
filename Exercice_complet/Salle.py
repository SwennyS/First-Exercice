# -*-coding:UTF-8 -*
"""Classe pour GROUPE 6
"""
from Destination import Destination
from types import *


class Salle:
	"""Classe Salle (int, salles|None, Destination.constante (see Destination for choices))
	"""

	def __init__(self, numero, salles, destination):
		
		assert type(numero) is IntType , "numéro doit être un entier"

		if salles is not None:
			if len(salles) != 0:
				for salle in salles:
					assert salle.numero != numero, "Identifiant de salle déjà existant!" 
				self.__numero = numero
		else :
			self.__numero = numero

		self.__destination = destination

		self.__tables = []

		self.__sieges = []

		self.__videoproj = None

		self.__ordinateurs = []


	def __getNumero(self):
		return self.__numero
	numero = property(__getNumero)


	def __getTables(self):
		return self.__tables
	tables = property(__getTables)


	def __getVideoproj(self):
		return self.__videoproj

	def __setVideoproj(self, videoproj):
		if(__videoproj is None):
			self.__videoproj = videoproj
		else:
			print ("Il existe déjà un video projecteur")
	videoproj = property(__getVideoproj, __setVideoproj)


	def findTable(self, num_table):
		for table in self.__tables:
			if table.numero == num_table:
				return table
		return None

	def addTable(self,table):
		self.__tables = Table()

	def removeTable(self, num_table):
		for table in self.__tables:
			if table.numero == num_table:
				self.__tables.remove(table)
				return True
			else:
				return False

	# def emptyTables(self):
	# 	self.__tables = []

	# def __getSieges(self):
	# 	return __sieges
	# sieges = property(__getSieges)

	# def addSiege(self, siege):
	# 	self.__sieges.append(siege)

	# def removeSiege(self, num_siege):
	# 	for siege in self.__sieges:
	# 		if siege.numero == num_siege:
	# 			self.__sieges.remove(siege)
	# 			return True
	# 	return False


	# def findOrdinateur(self, num_ordinateur):
	# 	for ordinateur in self.__ordinateurs:
	# 		if ordinateur.numero == num_ordinateur:
	# 			return ordinateur
	# 	return None


	def addOrdinateur(self, ordinateur):
		self.__ordinateurs.append(ordinateur)
		print("Ordinateur ajouté")


	def removeOrdinateur(self, num_ordinateur):
		for ordinateur in self.__ordinateurs:
			if ordinateur.numero == num_ordinateur:
				self.__ordinateurs.remove(ordinateur)
				print("Ordinateur supprimé")
				return True
		print("Impossible de supprimer l'oridnateur (id incorrect?)")
		return False

	# def emptyOrdinateurs(self):
	# 	self.__ordinateurs = []
