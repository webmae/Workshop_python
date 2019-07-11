#coding:utf-8

"""
Nommer une variable : doit commencer par une lettre ou un underscore 
                      ne pas contenir de caractères spéciaux
                      ne pas contenir d'espaces
                      utiliser des underscores (' _ ')

Types standards     : integer (int)
                    : nombre flotant (float)
                    : chaînes de caractères (str)
                    : booléen (bool)
                    : autres (liste, dictionnaire, tuple)

Fonctions basiques  : print()  => afficher à l'écran
                    : input()  => lire clavier
                    : type()   => retourne le type de données (variable, etc...)
                    : int(), float(), str(), bool() => convertir une données en une autre  ( une entré str " 25 " en int ) 
                    : str.format()  => ajouter une valeur dans une chaine de caractères
"""

agePersonne = 22  #variable de type int
prixHT = 120.5    #variable de type float
nom_personne = "perry"  #variable de type str ( chaîne de caractères )
continuer_Parti = True # booléen commence toujours par une majuscule

#===========================================================================#

print(type(agePersonne))
print(type(continuer_Parti))

print('\n') #  retour à la ligne

print('age de la personne =', agePersonne,".")
#python3 ajoute directement un espace entre la fin et la suite d'une chaîne de caractères

text = "hello, je suis {} et j'ai {} ans."
print(text.format(nom_personne,agePersonne))
#format permet de placer des valeurs dans une chaîne de caractères

print("hello, je suis {} et j'ai {} ans".format(nom_personne,agePersonne))
#plus court qu'au deçu

print('\n')

PlayerName = input("quel est ton nom ? : ")
print("bienvenu,",PlayerName)

print('\n')

#===========================================================================#
prixTc = input("entrez un nombre")
prixTc = int(prixTc)# je transforme la valeur de prixTc qui était une str en un int pour pouvoir la calculer

prixHT = prixTc + (prixTc*20 / 100)
print("prixHt = ",prixHT)

valeur_boolen = True
print(valeur_boolen)
valeur_boolen = int(valeur_boolen)
print(valeur_boolen)