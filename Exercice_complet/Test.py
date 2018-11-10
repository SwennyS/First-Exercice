# -*-coding:UTF-8 -*
"""Test pour UML
"""

"""Attention ! Bien vérifier que toutes les fonctions soient bien activees dans les différentes class. Notamment la classe 'Salle' qui contient l'essentiel des fonctions"""

from Salle import Salle
from Destination import Destination
from Etage import Etage
from Affectation import Affectation
from Ordinateur import Ordinateur
from CarteRes import CarteRes
from TypeRes import TypeRes
from Table import Table
from TypeSiege import TypeSiege
from Siege import Siege
from VideoProj import VideoProj

class Test:
	salle1 = Salle(10, None, Destination.CLASSE)
	print(salle1.numero)
	
	
	

	# salle2 = Salle(12, None, Destination.CLASSE)
	# print(salle2.numero)
	# salle3 = Salle(10, [salle1, salle2], Destination.CLASSE)
	# print(salle3.numero)


	# etage1 = Etage(1,200,None,Affectation.COURS)
	# print(etage1.numero)
	# print(etage1.surfaceSalleMoyenne())
	# etage1.addSalle(10, Destination.CLASSE)
	# print(etage1.findSalle(10).numero)
	# print(etage1.surfaceSalleMoyenne())
	# etage2 = Etage(1,20,[etage1],Affectation.ADMINISTRATION)


	ordi1 = Ordinateur(20,"Intel", "DDR4 8Go", 256.2, 10022018, "e6:f5:12", "56.23.33.33", "e5:f2", "56.23.32.32", None)
	print(ordi1.ram)		
	ordi1.addCarteRes("d3:12", "192.168",TypeRes.ETHERNET)
	ordi1.addCarteRes("d3:02", "192.167",TypeRes.WIFI)
	
	print("VideoProj :")
	videoproj1 = VideoProj(3, "VJ200", 6000, 1000, None)
	print(videoproj1.duree_ampoule)
	
	print("\n") #Saut de ligne
	print("\n") #Saut de ligne
	
	print("Affichage des tables :")		
	table1 = Table(1, 60, 150, None)
	print(table1.numero)
	table10 = Table(10, 60, 150, None)
	print(table1.largeur)
	table11 = Table(11, 50, 120, None)
	print(table11.longueur)
	table12 = Table(12, 100, 200, None)
	print(table12.numero)
	table13 = Table(13, 80, 220, None)
	print(table13.longueur)
	
	print("\n") #Saut de ligne
	print("\n") #Saut de ligne
	
	print("Siege :")
	siege1 = Siege(2,TypeSiege.ACCOUDOIR, None) 
	print(siege1.type_siege)
	siege2 = Siege(21, TypeSiege.SIMPLE, None)
	print(siege2.type_siege)
	siege3 = Siege(23, TypeSiege.FAUTEUIL, None)
	print(siege3.type_siege)
	siege4 = Siege(24, TypeSiege.SIMPLE, None)
	print(siege4.type_siege)
	
	print("\n") #Saut de ligne
	print("\n") #Saut de ligne
	
	salle1.addOrdinateur(ordi1)
	salle1.removeOrdinateur(1)
	
	
	
