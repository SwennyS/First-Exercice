# -*-coding:UTF-8 -*
"""Fonction pour le matériel (classe Salle)


#Siege

	def __init__(self):
		self.__sieges = []

	def get_sieges(self):
		return self.__sieges
		
	def find_siege(self, numero_siege):
		for siege in self.__sieges:
			if siege.numero == numero_siege:
				return siege
		return None
		
	def add_siege(self, siege):
		self.__sieges.append(siege)
		
	def remove_siege(self, numero_siege):
		for siege in self.__sieges:
			if siege.numero == numero_siege:
				self.__sieges.remove(siege)
				return True
		return False
		
	def empty_sieges(self):
		self.__sieges.clear()
		

#Table


	def __init__(self):
		self.__tables = []

	def get_tables(self):
		return self.__tables
		
	def find_table(self, numero_table):
		for table in self.__tables:
			if table.numero == numero_table:
				return table
		return None
		
	def add_table(self, table):
		self.__tables.append(table)
		
	def remove_table(self, numero_table):
		for table in self.__table:
			if table.numero == numero_table:
				self.__tables.remove(table)
				return True
		return False
		
	def empty_tables(self):
		self.__tables.clear()
		
		
#VideoProjecteur

	def __init__(self):
		self.__videoprojecteurs = []

	def get_videoprojecteurs(self):
		return self.__videoprojecteurs
		
	def find_videoprojecteur(self, numero_videoprojecteur):
		for videoprojecteur in self.__videosprojecteurs:
			if videoprojecteur.numero == numero_videoprojecteur:
				return videoprojecteur
		return None
		
	def add_videoprojecteur(self, videoprojecteur):
		self.__videosprojecteurs.append(videoprojecteur)
		
	def remove_videoprojecteur(self, numero_videoprojecteur):
		for videoprojecteur in self.__videoprojecteur:
			if salle.videoprojecteur == numero_videoprojecteur:
				self.__videoprojecteurs.remove(videoprojecteur)
				return True
		return False
		
	def empty_videoprojecteurs(self):
		self.__videoprojecteurs.clear()
		
		
#Ordinateur

	def __init__(self):
		self.__ordinateurs = []

	def get_ordinateurs(self):
		return self.__ordinateurs
		
	def find_ordinateur(self, numero_ordinateur):
		for ordinateur in self.__ordinateurs:
			if ordinateur.numero == numero_ordinateur:
				return ordinateur
		return None
		
	def add_ordinateur(self, ordinateur):
		self.__ordinateurs.append(ordinateur)
		
	def remove_ordinateur(self, numero_ordinateur):
		for ordinateur in self.__ordinateur:
			if ordinateur.numero == numero_ordinateur:
				self.__ordinateurs.remove(ordinateur)
				return True
		return False
		
	def empty_ordinateurs(self):
		self.__ordinateurs.clear()
