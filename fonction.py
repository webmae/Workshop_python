#coding:utf-8

"""
Fonctions vues: print(), input(),type(),int(),float(),str(),bool()
"""

age = input("quel âge as-tu ? ")
age = int(age)

print("tu as",age,"ans.")

def dire_bonjour(): # déclaration d'une fonction sans paramétre, attention aux tabulations/espaces
    print("bonjour world") #action que va faire la fonction

dire_bonjour() #appel de la fonction

print("\n")

def dire(nom,message):
    print("{} dit {}".format(nom,message))

dire("perry","salut") #ces deux paramètres sont des chaînes de caractères


def dire_deux(nom="perry",message="salut"): # vous pouvez aussi directement donner des valeurs aux paramètres
    print("{} dit {}".format(nom,message))

dire_deux()
dire_deux("robert") # à ce moment là, le paramètre nom prendra la valeur que vous lui donnez dans l'appel de la fonction



print("\n")


def dire_trois(nom="perry",age=22,message="salut"):
    print("{} dit qu'il a {} ans et {}".format(nom,age,message))#python suit l'ordre des paramètres mais vous pouvez les changer de place comme bon vous sembles
    print("{} dit qu'il a {} ans et {}".format(age,age,message))
    

dire_trois()

print("\n")

def liste_inventaire(*items):# '*' siginifie qu'il peut y avoir un nombre infini de paramètres
    for ittems in items:
        print(ittems)

liste_inventaire("épée")
liste_inventaire("épée","bouclier","potions","dague","fromage")


print("\n")

def somme(nb1,nb2): #cette fonction return un résultat et vous pourrez l'afficher en appelant la fonction dans un print()
    rslt = nb1+nb2
    return rslt

print(somme(4,4))


def compare(nb1,nb2):
    if nb1 < nb2:
        return nb1
    elif nb1 > nb2:
        return nb2
    else:
       return "égale"

print(compare(5,5))

print("\n")



def iterative_factorial(nb):#une fonction itérative, utilise une boucle
    rslt = nb
    if nb == 0:
        print("0")
    elif nb == 1:
        print(nb)
    else:
        while nb != 1:
            rslt = rslt*(nb-1)
            print(rslt)
            nb-=1

iterative_factorial(5)

print("\n")




def recursive_factorial(nb):#une fonction récursive se rapelle elle-même
    if nb == 0:
        return 1
    else:
        return nb*recursive_factorial(nb-1)

print(recursive_factorial(5))