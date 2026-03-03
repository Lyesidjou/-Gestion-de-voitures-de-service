class Employe():
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


