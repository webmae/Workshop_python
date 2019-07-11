#coding:utf-8

"""
Opérateurs de comparaisons : == ( égale à )
                             != ( différent de )
                             < ( plus petit que )
                             > ( plus grand que )
                             <= ( plus petit que )
                             >= ( plus grand que )

Mots clés des conditions    : if / elif / else

Conditions multiples        : and ( et )
                              or ( ou )
                              in / not in (dans / pas dans )
                              not ( ce n'est pas ex: if not ...)

"""

identifiant = "perry"
mot_de_passe = "123"

print("interface de connexion")

user_id = input("entrez votre id")
user_password = input("entrez votre mop de passe")

if user_id == identifiant and user_password == mot_de_passe: #condition avec "and" car il faut que les deux variables soit vrai
    print("vous êtes connectés, bienvenu",user_id)
else:
    print("identifiant ou mot de passe incorrecte")

print("je ne suis plus dans la condition if")

print("\n")





lettre_hasard = "i"
if lettre_hasard in "aeiouy": # si "i" est dans cette string, sa affichera que c'est une voyelle
    print(" {} est un voyelle".format(lettre_hasard))

if lettre_hasard not in "aeouy": # si "i" n'est pas dans la string, cela affichera que c'est une consonne
    print("{} est une consonne".format(lettre_hasard))

print("\n")






lettre_hasard = "i"
if lettre_hasard in "aeiouy":
    print("{} est une voyelle".format(lettre_hasard))
else:
    print('{} est une consonne'.format(lettre_hasard))


print("\n")





age = input("entre ton âge : ")
age = int(age)
if age == 18:
    print("tu es majeur")
elif age < 18:
    print("tu es mineur")
elif age > 60:
    print("tu es vieux")
else:
    print("tu as ",age)


print("\n")






jeu_charge = True

if jeu_charge:
    print("le jeu est chargé")
else:
    print("le jeu n'est pas chargé")

if not jeu_charge:
    print("le jeu n'est pas chargé")
else:
    print("le jeu est chargé")

print("\n")


    


age_deux = input("quel âge as-tu ? ")
age_deux = int(age_deux)

if age_deux > 0 and age_deux < 100:
    print("âge validé")
else:
    print("âge non validé")


if 0 < age_deux < 100:
    print("âge validé")
else:
    print("âge non validé")

