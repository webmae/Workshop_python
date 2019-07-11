#coding:utf-8

"""
Boucles   : while / for
Mots clés : break ( casse la boucle ) / continue ( revient au début de la boucle) 
"""

jeu_lance = True
print("")

while jeu_lance:
    choixMenu = input("> ")

    if choixMenu == "again": # si vous ecrivez "again" la boucle continue
        continue
    elif choixMenu == "quit": # si vous ecrivez "quit", choixMenu deviendra False donc la boucle s'arrêtera
        jeu_lance = False
    elif choixMenu == "hello": # si vous ecrivez "hello", la boucle vous répondra "bonjour"
        print("bonjour")
    else:
        print("commande introuvable")

print("à bientôt")

print("\n")

phrase = "bonjour"

for letter in phrase: # cette boucle, va vérifier chaque caractères dans la string de la variable phrase
    print(letter)