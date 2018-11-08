#exercice UML

class Etablissement:
	def __init__(self, Etage, Salle,nb_etage):
		self.etage = Etage
		self.salle = Salle
		self.nbetage = 0
		
class Etage:
	def __init__(self, Numero, Salle):
		self.numero = 0
		self.salle = Salle
		self.surface = 0.2
		self.type = type
		
class Salle: 
	def __init__(self, Numero):
		self.numero = 0
		self.type = type
		self.liste_materiel = []
	
	
class Cours:
	def __init__(self, Id):
		self.id = 0 
		self.nom = nom
		self.nb_seance = 0
		self.nb_heure = 0
	
class Siege:
	def __init__(self, Numero):
		self.numero = 0
		self.type = type
		Salle.liste_materiel = self.numero 
		
	
class Table:
	def __init__(self, Numero):
		self.numero = 0
		self.largeur = 0.1
		self.longueur = 0.1
		Salle.liste_materiel = self.numero
			
class VideoProjecteur:
	def __init__(self, Numero):
		self.numero = 0
		self.nom_modele = type
		self.luminosite = 0
		self.duree_vie = 0
		Salle.liste_materiel = self.numero
		
	
	
class Ordinateur:
	def __init__(self, Numero, Carte, Microprocesseur, MemoireVive, CapaciteDisqueDur):
		self.numero = 0
		self.carte = Carte
		self.microprocesseur = type 
		self.memoire_vive = 0
		self.capacite_disque_dur = 0.2
		self.date_achat = 01/01/2000
		
		
class Carte:
	def __init__(self, Type, NumeroIp, NumeroMac):
		self.type = type
		self.numero_ip = 0
		self.numero_mac = 0
