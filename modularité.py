#coding:utf-8

"""
Importer un module : import <nom_module>
                     from <nom_module> import <nom_fonction>
                     from <nom_module> import *
"""
#ce module est dans le même dossier que le fichier modularité.py
import module as mod # si vous devez utiliser plusieurs fois le module, vous pouvez le renomé 
import math
import os

mod.somme(1,2) #une fois le module importé, il faut l'appeller avec la fonction




rslt = math.sqrt(100) #utilise la fonction sqrt du module math qui donne la racine carré d'un nb
print(rslt)



print("\n")

coucou = lambda : print("bonjour")#lambda est une fonction qui simple qui fait toujours la même chose

coucou()

print("\n")


ttc = lambda prixHt : prixHt + (prixHt * 20 / 100) # prixHt = paramètre de la fonction lambda

print(ttc(24))

print("\n")

calculer = lambda a,b : a + b

print(calculer(5,2))


#os.system("cls")#clear terminal

mod.au_revoir()