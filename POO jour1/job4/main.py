class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return f"Je suis {self.nom} {self.prenom}"

# Création d'objets de la classe Personne
personne1 = Personne("Doe", "John")
personne2 = Personne("Dupond", "Jean")

# Affichage des présentations des personnes
print(personne1.SePresenter())
print(personne2.SePresenter())