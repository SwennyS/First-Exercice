# -*-coding:UTF-8 -*
"""Classes pour les stations
"""

	

class Station:
	"""Classe Station
	"""
	
	def __init__(self):
		self.__velos = []

	def get_velos(self):
		return self.__velos
		
	def find_velo(self, num_velo):
		for velo in self.__velos:
			if velo.numero == num_velo:
				return velo
		return None
		
	def add_velo(self, velo):
		self.__velos.append(velo)
		
	def remove_velo(self, num_velo):
		for velo in self.__velo:
			if velo.numero == num_velo:
				self.__velos.remove(velo)
				return True
		return False
		
	def empty_velos(self):
		self.__velos.clear()


		
		
		
		
		
		
		
		
		
		