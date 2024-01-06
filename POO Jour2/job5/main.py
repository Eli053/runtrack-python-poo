class Voiture:
    def __init__(self, marque='', modele='', annee=0, kilometrage=0):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50

    # ... autres méthodes ...

    def demarrer(self):
        if self.__verifier_plein():
            self.__en_marche = True
        else:
            print("Erreur : Le réservoir est vide.")

    def arreter(self):
        self.__en_marche = False

    def __verifier_plein(self):
        return self.__reservoir > 5

# Instanciation de la classe Voiture
voiture = Voiture('Peugeot', '208', 2020, 15000)

# Appel des méthodes
voiture.demarrer()
