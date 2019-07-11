#coding:utf-8

"""
(!) Tuples : conteneur immuable (dont on ne peut modofier les valeurs )

Création de tuples  : mon_tuples = () // vide
                    : mon_tuples = 17 // une seul valeur
                    : mon_tuples = (17,) // pareil qu'au dessus. Attention à mettre la virgule car sans elle, ce n'est pas un tuple mais un int
                    : mon_tuples = (1,2,3) // plusieurs valeurs

Accès au xvaleurs   : mon_tuples[x] // valeur d'indice x

2 raisons d'utiliser les tuples : affectation multiple de variable
                                : retour multiple de fonction
""" 

liste = [1,2,3,4,5,6,7,8,9]

for choses in enumerate(liste): #enumerate donne les indices des valeurs de la liste
    print(choses)

print("\n")

mon_tuple = (48)
print(type(mon_tuple))

print('\n')

mon_tuple2 = (17,)
print(type(mon_tuple2))

mon_tuple3 = (1,2,3,4,5,6,7,8,9)
print(type(mon_tuple3))

print('\n')

(nb1,nb2) = (2,8)  # ce n'est pas un tuple 
#print(type(nb1,nb2)) # vous aurez une erreur de type car 'type" prend un argument
print(nb1)
print(nb2)

(nb3,nb4) = 2,5
print(nb3)
print(nb4)

nb1 = 125
print(nb1)

print("\n")

mon_tuple4 = ("pomme","banane","fraise")
print(mon_tuple4)
#mon_tuple4[2] = "orange" # vous aurez une erreur de type car on ne peut pas changer une valeur dans un tuple
print(mon_tuple4)


print("\n")

def getPlayer_position():
    posX = 145
    posY = 125
    return(posX,posY)


coordX = 0
coordY = 0

print("position du joueur : ({}/{})".format(coordX,coordY))

(coordX,coordY) = getPlayer_position()

print("position du joueur : ({}/{})".format(coordX,coordY))