#coding:utf-8
import copy
"""
list[x]     : affiche l'élément d'indice x
list[-x]    : affiche xéme élément en partant de la fin
list[:]     : affiche tous les éléments
list[:x]    : affiche les x premiers éléments
list[x:]    : affiche les x derniers éléments
list[a : b] : affiche de l'élément d'indice a (non inclus) à l'éléments b 
"""

#création d'une liste
inventaire = list()
inventaire2 = []
print(type(inventaire))
print(inventaire)

print("\n")

print(type(inventaire2))
print(inventaire2)

print("\n")

inventaire3 = ["ok",2,"hello"]
print(inventaire3,"\n")

inventaire4 = [0]*10 #ajouteras 10 fois le caractères 0
print(inventaire4,"\n")

inventaire5 = range(0,20)
i = 0
while i < len(inventaire5):
    print(inventaire5[i])
    i+=1

print("\n")

list_equip = ["épée","bouclier","arc","potion","tunique"]
for valeur in list_equip:
    print(valeur,"\n")

print(list_equip[:])
print(list_equip[:2])
print(list_equip[2:])
print(list_equip[-2])
print(list_equip[2:4])

print(list_equip)
list_equip = "bonbon"
print("\n")

list_L = ["j'ai un bouclier d'or"]
print(list_L)

if "bouclier" in list_L:
    print("j'ai un bouclier")
else:
    print("je n'ai pas de bouclier")

print("\n")

list_food = ["tomate","cerise"]
print(list_food)
list_food.append("carotte")
print(list_food)
list_food.insert(2,"oignon")# le premier argument, indique la place où inserer la valeur
print(list_food)


print("\n")

list_food.remove("tomate")
print(list_food)

del list_food[1]# le numéro indique la valeur a supprimer via l'indice
print(list_food)

listAnimaux = ["chien","chat","oiseaux","herisson","poisson"]
print(listAnimaux)
animaux_a_supprimer = listAnimaux.index("chat")
print(animaux_a_supprimer)
del listAnimaux[animaux_a_supprimer]
print(listAnimaux)

print("\n")

listAnimaux.sort()#tri la list par ordre alphabétique
print(listAnimaux,"\n")


listAnimaux.reverse()#retourne le contenue de la list
print(listAnimaux)

list_couleur = ["bleu","vert","rouge","mauve","orange"]
print(list_couleur)

print("il y a", list_couleur.count("bleu"),"couleurs les mêmes")#calcul le nombre d'occurence dans la list

list_couleur.clear()
print(list_couleur)# list_couleur[:]  = []

chaine_bonjour = ["bonjour","les","gars"]
phrase = " ".join(chaine_bonjour) # permet de donner les valeurs de la list à une variable
print(phrase)

list1 = ["epee","casque","plastron"]
print(list1)
list2 = list1
print(list2)

list2.append("botte") #pas bien car on change aussi les valeurs de la list1

print(list1)
print(list2)

#il faut copier la list et modifier la copie

list3 = ["epee","sabre","arme","orbe"]
list4 = copy.deepcopy(list3)# import deepcopy avec le module copy 

print(list3)
print(list4)

list4.append("ok")

print(list3)
print(list4)


list_lettre = ["h","e"]
list_lettre2 = ["l","l","o"]

print(list_lettre)
print(list_lettre2)

list_lettre.extend(list_lettre2)#ajoute une liste à la suite d'une autre

print(list_lettre)

print("\n")

list_test = [1,2,"e",3,4,5,6,7,8,9]
print(list_test[:3])
print(list_test[3:])
print(list_test[:])
print(list_test[-1])
print(list_test[-2])
print(list_test[1:9])