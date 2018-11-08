#Commentaire

#from velov.Velo import *

class Polygone:
	
	TAUX = 0.2
	
	def __init__(self) :
		self.couleur = 'bleu'
		
mon_polygone = Polygone()
print(mon_polygone.couleur)
print(Polygone.TAUX)

class Octogone(Polygone) :
	def __init__ (self) :
		Polygone.__init__(self)
		
octo = Octogone()
print(octo.couleur)

		





