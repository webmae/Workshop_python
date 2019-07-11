#coding:utf-8

"""
Fonctions utiles : isinstance (<objet>, <classe>) : vérifie qu'un objet est de la classe renseignée
                 : issubclass (<class_fille>, <class_mere>) : verifie qu'une classe est fille d'une autre
"""
class Vehicule():
    def __init__(self,nom_vehicule,quantite_essence):
        self.nom = nom_vehicule
        self.essence = quantite_essence

    def deplacer(self): #méthode
        print("le vehicule {} se déplace".format(self.nom))

class Voiture(Vehicule):
    def __init__(self,nom_voiture,essence,puissance):#nous reprenons des attributs de la class mère et en rajoute selon la class créée
        Vehicule.__init__(self,nom_voiture,puissance)# avec Vehicule, nous reprenons les attributs de la class mère 
        self.puissance = puissance 

    def deplacer(self):
        print("je roule ...")


class Avion(Vehicule):
    def __init__(self,nom,essence,marchandise):#nous reprenons des attributs de la class mère et en rajoute selon la class créée
        Vehicule.__init__(self,nom,essence)
        self.marchandise = marchandise

    def deplacer(self):
        print("je vole dans les airs...")

voiture1 = Voiture("ford",90,420)
voiture1.deplacer()
print(voiture1.puissance)# affiche la puissance de la voiture de la class Voiture
av1 = Avion("f22",2400,"missiles")
av1.deplacer()

print("\n")

class Animal():
    def __init__(self,nom):
        self.nom = nom

    def manger():
        print(self.nom,"mange")

    
class Reptil(Animal):
    def __init__(self,nom,regime_alimentaire):
        Animal.__init__(self,nom)
        self.regime = regime_alimentaire

    def manger(self):
        print("le reptile mange...")

    
lezard = Reptil("lezrd","grenouille")
lezard.manger()
print(isinstance(lezard,Animal))

if isinstance(lezard,Animal):
    print("lezard est un anmal")