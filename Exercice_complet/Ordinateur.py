# -*-coding:UTF-8 -*
"""Classes pour GROUPE 6
"""

from CarteRes import CarteRes
from types import *

class Ordinateur:
	"""Classe Ordinateur
	"""
	
	def __init__(self, num_ordi, micro_proc, ram, capacite, date_achat, mac_eth, ip_eth, mac_wifi, ip_wifi, ordinateurs):
		
		# Assertion principle : we write what we want to have, here, a positive surface value.
		assert type(num_ordi) is IntType , "num_ordi doit être un entier!" 
		assert type(micro_proc) is StringType , "micro_proc doit être une chaine de caractères!" 
		assert type(ram) is StringType , "ram doit être une chaine de caractères!" 
		assert type(capacite) is FloatType , "capacite doit être un flottant!" 
		# assert type(date_achat) is StringType , "La date ne peut être négative!" 
		assert type(mac_eth) is StringType , "mac_eth doit être une chaine de caractères!" 
		assert type(ip_eth) is StringType , "ip_eth doit être une chaine de caractères!" 
		assert type(mac_wifi) is StringType , "mac_wifi doit être une chaine de caractères!" 
		assert type(ip_wifi) is StringType , "ip_wifi doit être une chaine de caractères!" 


		if ordinateurs is not None:
			if len(ordinateurs) != 0:
				for numeroOrdinateur in ordinateurs.numero:
					assert numeroOrdinateur != num_ordi, "Identifiant d'ordinateur déjà existant!" 
				self.__numero = num_ordi
		else :
			self.__numero = num_ordi


		self.__micro_proc = micro_proc

		self.__ram = ram

		self.__capacite = capacite

		self.__data_achat = date_achat

		self.__cartes_res = []


	def __getNumero(self):
		return self.__numero
	numero = property(__getNumero)

	def __getMicroProc(self):
		return self.__micro_proc
	micro_proc = property(__getMicroProc)

	def __getRam(self):
		return self.__ram
	ram = property(__getRam)

	def __getCapacite(self):
		return self.__capacite
	capacite = property(__getCapacite)

	def __getDataAchat(self):
		return self.__data_achat
	date_achat = property(__getDataAchat)

	def __getCartesRes(self):
		return self.__cartes_res
	cartes_res = property(__getCartesRes)


	def addCarteRes(self,mac,ip,type_res):
		if len(self.__cartes_res) >= 2:
			print("Impossible d'ajouter une carte supplémentaire, déjà 2 existantes.")
		else:
			if (len(self.__cartes_res) > 0):
				self.__cartes_res.append(CarteRes(mac,ip,type_res,self.__cartes_res))
			else:
				self.__cartes_res.append(CarteRes(mac,ip,type_res,None))
			# if len(self.__cartes_res) > 0:
			# 	for carte_res in self.__cartes_res:
			# 		assert carte_res.type_res != type_res, "Une carte réseau de type est déjà installée dans l'ordinateur"
			# 	self.__cartes_res.append(CarteRes(mac,ip,type_res,self.__cartes_res))
			# else:
			# 	self.__cartes_res.append(CarteRes(mac,ip,type_res,self.__cartes_res))
