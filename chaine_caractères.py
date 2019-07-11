#coding:utf-8

"""
Une méthode de chaîne travaille sur une copie, et pas sur la chaîne elle-même

classe str  : string (chaîne de caractères)

str.upper()  : mets la chaine en majuscule
str.lower()  : mets la chaîne en minuscule
str.capitalize() : mets la première lettre de la chaîne en majsucule
str.title()  : mets chaque première lettre en majuscule
str.center(<largeur>, <caractère_remplissage>) :  ajoutes des caractères pour que le text soit au centre
str.find(<chaîne>,<début>,<fin>) : cherche les caractères demandé
str.index(<chaîne>,<début>,<fin>) : chercher les caractères demandé
str.strip() : retire les espaces avant/après 
str.replace(<ancien caractères>,<nouveaux caractères>,<occurence>) : remplace certains caractères par d'autres


str.isalpha() : vérifie si la chaîne ne contient que des caractères alphabétique
str.isditgit() : vrifie si la chaîne ne contient que des caractères numérique
str.isdecimal() : vérifie si  la chaîne ne contient que des caractères décimaux . Présent uniquement sur les objets unicode
str.isnumeric() : vérifie si  la chaîne ne contient que des caractères numérique . Présent uniquement sur les objets unicode
str.isalphanum() : vérifie si la chaîne est composé de caractères alphanumérique
str.islower() : vérifie si il y a des caractères en majuscule 
str.isupper() : vérifie si il y a des miniscule
str.isidentifier(): vérifie si une des chaînes de caractères n'est pas un mot spécifique à Python

"""

#help(str) dans le terminal
maChaine = "hello world"
maChaine = maChaine.upper()

maChaine2 = "salit les GARS"
maChaine2 = maChaine2.lower()

maChaine3 = "hello les petits becodiens"
maChaine3 = maChaine3.capitalize()

maChaine4 = " ok ok ok ok ok ok"
maChaine4 = maChaine4.title()

print(maChaine)
print("\n")
print(maChaine2,"\n")
print(maChaine3,"\n")
print(maChaine4,"\n")

ch1 = "bonjour"
ch2 = ch1

print(ch1)
print(ch2,"\n")

ch1 = ch1.upper()

print(ch1)
print(ch2,"\n")

maChaine5 = "monSuperProGramme"
print(maChaine5,"\n")

maChaine5 = maChaine5.center(50,'-')

print("\n")

maChaine6 = "Super gros"
print(maChaine6)
print(maChaine6.find("gros"))

print("\n")

maChaine7 = "va te faire"
print(maChaine7,"\n")

try:
    print(maChaine7.index("gros"))
except ValueError:
    print("je n'ai pas trouvé cette chaîne\n")

maChaine8 = "          salut les gros gars"
print(maChaine8)
print(maChaine8.strip())

print("\n")

maChaine9 = "et oh lets go"
print(maChaine9)
maChaine9 = maChaine9.replace("e","z",2)
print(maChaine9,"\n")

maChaine10 = "Magicien|10|5"
print(maChaine10.split("|"))
print("\n")

maChaine11 = "Bonjour"
if maChaine11.islower():
    print("Minuscule")
else:
    print("la chaîne contient des majuscule")

print("\n")


maChaine12 = "class"
if maChaine12.isidentifier():
    print("reservé")
else:
    print("ce mot n'est pas réservé")

print("\n")

maChaine13 = "le langage python"
if "langage" in maChaine13:
    print("langage")
else:
    print("non trouvé")

print("\n")

maChaine14 = "comment vas tu ?"
print(maChaine14)
print(maChaine14.islower())
