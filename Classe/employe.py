from personne import Personne

class Employe(Personne):
    def __init__(self,noEmploye: int,nas:int):
        self.noEmploye = noEmploye
        self.nas = nas