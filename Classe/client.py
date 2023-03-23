from personne import Personne

class Client(Personne):
    def __init__(self, numeroIdentification: str, sexe: str):
        self.numeroIdentification = numeroIdentification
        self.sexe = sexe

