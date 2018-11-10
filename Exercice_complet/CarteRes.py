# -*-coding:UTF-8 -*
"""Classes pour GROUPE 6
"""

from types import *

class CarteRes:
	"""Classe CarteRes
	"""
	
	def __init__(self,mac,ip, type_res, cartes_res):
		
		# Assertion principle : we write what we want to have, here, a positive surface value.
		assert type(mac) is StringType , "mac doit être une chaine de caractères!" 
		assert type(ip) is StringType , "ip doit être une chaine de caractères!" 

		if cartes_res is not None:
			if len(cartes_res) != 0:
				for carte_res in cartes_res:
					assert carte_res.mac != mac, "Addresse MAC déjà existante!" 
				self.__mac = mac
		else :
			self.__mac = mac

		self.__ip = ip

		self.__type_res = type_res


	def __getMAC(self):
		return self.__mac
	mac = property(__getMAC)

	def __getIP(self):
		return self.__ip
	ip = property(__getIP)

	def __getTypeRes(self):
		return self.__type_res
	type_res = property(__getTypeRes)