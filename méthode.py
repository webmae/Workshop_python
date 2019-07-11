#coding:utf-8

"""
Méthode           : fonction sur une classe (objet)
Méthode de classe : fonction sur une classe
Méthode statique  : fonction indépendante mais "lié" à une classe
"""

"""méthode"""

class Humain:
    #classe qui définit un humain

    lieu_habitation = "terre"

    def __init__(self,nom,age):
        self.nom = nom
        self.age = age

    def parler(self,message):
        print("{} a dit : {}".format(self.nom,message))

    def changer_planee(cls,nouvelle_planete):#cls = métode de classe
        Humain.lieu_habitation = nouvelle_planete

    changer_planee : classmethod(changer_planee)#cela définit une méthode de classe

    def definition():
        print("l'Humain est classé étant le plus haut être-vivant dans la chaîne alimentaire")

    definition = staticmethod(definition)

h1 = Humain("perry",22)# obliger de créer une instance avant

h1.parler("bonjour b")

print("\n")