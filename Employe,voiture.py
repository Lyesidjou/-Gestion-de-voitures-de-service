class Employe():
    def __init__(self, numeroPermis:str, nom:str, prenom:str):
        self.numeroPermis = numeroPermis
        self.nom = nom
        self.prenom = prenom
        self.voitureService= None
    def afficher_informations(self):
        print(f"l'Employe qui as le numero de permis {self.numeroPermis} est nomee {self.nom} {self.prenom}")
class Voiture:
    def __init__(self, matricule:str,annee:int, marque:str,kilometrage:int):
        self.matricule = matricule
        self.annee = annee
        self.marque = marque
        self.kilometrage = kilometrage
        self.chauffeur = None