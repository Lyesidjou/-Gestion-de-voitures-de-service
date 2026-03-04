class Employe:
    def __init__(self, numeroPermis:str, nom:str, prenom:str):
        self.numeroPermis = numeroPermis
        self.nom = nom
        self.prenom = prenom
        self.voitureService = None
    def affecter_voiture(self, voiture):
        if self.voitureService==None:
            if voiture.chauffeur==None:
                self.voitureService = voiture
                voiture.chauffeur = self
            else:
                print("la voiture est attribue deja a un chauffeur")
        else:
            print("le chauffeur a deja un vehicule de service")
    def retirer_voiture(self):
        if self.voitureService!=None:
            self.voitureService.chauffeur=None
            self.voitureService = None
        else:
            print("voiture non disponible")
    def afficherInformations(self):
        print(f"l'employee qui possede le numero {self.numeroPermis} nomee {self.nom} {str(self.prenom)}")
        if self.voitureService!=None:
            print(f"le chauffeur possede la voiture immatriculé {self.voitureService.matricule} de la marque {self.voitureService.marque}")

class Voiture:
    def __init__(self, matricule:str, annee:int, marque:str, kilometrage:int):
        self.matricule = matricule
        self.annee = annee
        self.marque = marque
        self.kilometrage = kilometrage
        self.chauffeur = None
    def affecter_chauffeur(self):
        print(f"la voiture est immatricule {self.matricule} annee {self.annee} marque {self.marque} qui as parcorue {self.kilometrage}")
        if self.chauffeur!=None:
            print(f"le chauffeur de cette voiture est {self.chauffeur.nom} {self.chauffeur.prenom}")
        else:
            print("le chauffeur non disponible")
