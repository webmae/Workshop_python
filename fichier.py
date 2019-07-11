#coding:utf-8
import pickle
import codecs
"""
Mode d'ouverture : r ( lecture seul )
                 : w ( écriture avec remplacement )
                 : a ( écriture avec ajout en fin de fichier)
                 : x ( lecture et écriture )
                 : r+ ( lecture/écriture dans un même fichier)


Lecture          : read(), readline(), readlines()
Ecriture         : write()
"""

fic = open("fichier.txt",encoding="utf-8",mode="r") # création d'une variable qui ouvre le fichier txt (qui est dans le même dossier) en lecture seul

line = fic.readline() #affiche une ligne du fichier txt, une seul et la première qu'il rencontre
print(line)
lines = fic.readlines() # retourne le reste des lignes dans une liste avec, les retours à la ligne,etc...
print(lines)
print(lines[1]) # retourne la valeur d'indice donner de la liste créée par readlines()

fic.close() # fermer le fichier en cours

if fic.close: # moyen de vérifier si le fichier est fermé
    print("le fichier est fermé")
else:
    print("le fichier n'est pas fermé")

print("\n")

with open("fichier2.txt",encoding="utf-8",mode="r") as fiche:
    content = fiche.read() # pas besoin de fermer lors de l'utilisation de with
    if fiche.closed:
        print("fermé")
    else:
        print("fichier ouvert, il est dans le with")

if fiche.close:
    print("fichier fermé")
else:
    print("fichier toujours dan with")

print("\n")

with open("fichier2.txt",encoding="utf-8",mode="w") as fiiche:
    nb = 15
    fiiche.write(str(nb))
    fiiche.write("\n")
    fiiche.write("ok mec\n")
    fiiche.write("salut\n")


class Player():
    def __init__(self,name,level):
        self.name = name
        self.level = level

    def whoaim(self):
        print("{} ({})".format(self.name,self.level))

print("\n")

p1 = Player("perry",22)
p1.whoaim()

with open("Player.data","wb") as fic: # le "d" après  le w indique que c'est en binaire mode binaire
    record = pickle.Pickler(fic) # crée une variable qui va servir d'enregistrement
    record.dump(p1)# méthode qui va permettre une copie de l'objet

with open("Player.data","rb") as fic:
    get_record = pickle.Unpickler(fic)
    player_one = get_record.load()

player_one.whoaim()