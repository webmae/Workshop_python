#coding:utf-8

"""
Création d'un dictionnaire : dico = {} // vide. Le dico accepte tout les types de variables
                           : dico = {<clé> : <valeur>, <clé> :  <valeur>, ... : ...}

Accès à une valeur         : dico[<clé>]

Ajout et modification du dictionnaire : dico[<clé>] = <valeur>
                                      : dico.pop(<clé>)   // supprime la clé et la valeur var elles sont liées
                                      : del dico(<clé>)

Copie de dictionnaire                 : dico1 = {1:11, 2:22}
                                      : dico2 = dico1.copy()


"""

dico = {1:45, "prenom" : "perry"}
print(dico)
print(dico[1]) # affiche la valeur de la clé n°1
print(dico["prenom"]) # affiche la valeur de la clé "prenom"

print('\n')

dico3 = {}
dico3["chien"] = "c'est le meilleur ami de l'homme"
print(dico3["chien"])


print("\n")

dico4 = {"chat":"felin","chien":"canidé","baleine":"mammifère"}
print(dico4)
dico4.pop("chien") # suppression  de la clé chien et de sa valeur 
print(dico4)

print("\n")

dico5 = {"chat":"félin","chien":"canidé","baleine":"mammifère"}
print(dico5)
del dico5['chat']
print(dico5)

print("\n")

if "chien" in dico5:
    print("oui")
else:
    print("non")

print("\n")

dico6 = {1:2,2:3,3:4,4:5,5:6,6:7,7:8,8:9,9:10}
for key in dico6.keys(): # affiche les clés du dictionnaire
    print(key)

for values in dico6.values():# affiche les valeurs du dictionnaires
    print(values)

for k,v in dico6.items():
    print("clé = {} et valeurs = {}".format(k,v))

print('\n')

dico_doc = {"chat":"félin","chien":"canidé","baleine":"mammifère"}
dico_doc2 = dico_doc.copy()
print(dico_doc)
print(dico_doc2)

dico_doc2["humain"] = "cochon"
print(dico_doc)
print(dico_doc2)

print('\n')

def maFonctionDico(**parametres):#une fonction qui permet d'afficher un dictionnaire en paramètre
    print(parametres)

maFonctionDico(prenom="perry",nom="nowak",age="22")

    