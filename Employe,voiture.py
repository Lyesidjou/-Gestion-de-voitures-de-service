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
