#coding:utf-8

"""
classe    : plan de conception, genre ( ex : Humain)
objet     : instance d'uen classe ( ex : Julien est un objet de la classe Humain)
attribut  : variable de classe ( ex : prenom,nom,taille,sexe)
"""

class Humain():

    humain_creer = 0 #cette varaible est en dehors du concstructeur  attribut de classe
    def __init__(self, c_prenom, c_age):#self est l'objet de la classe, on le met toujours en première place
        print("création d'un humain",self) # le self ici, sert a vérifier que les humain créés sont bien des humains différents
        self.name = "perry"
        self.age = 22
        self.Age = c_age # Age appartient à la classe, alors que c-age est une paramètre
        self.Prenom = c_prenom
        Humain.humain_creer+=1

print("lancement du programme")

h1 = Humain("perry",22)
print("prénom de h1 -> {}".format(h1.name))# comme h1 = la classe Humain, il suffit d'aller chercher le self demandé en mettant h1.name
print("âge = {}".format(h1.age))
#ou
print("âge --> {}".format(h1.Age))
print("humain existant : {}".format(Humain.humain_creer))
print("\n")

h2 = Humain("yrrep",22)
print("humain existant = {}".format(Humain.humain_creer))

print("\n")

h3 = Humain("yrr",22)
print("humain existant = {}".format(Humain.humain_creer))