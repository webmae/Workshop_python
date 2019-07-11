#coding:utf-8

"""
Gérer les execptions  : try / execpt ( + else, finally)

Types d'execptions    : ValueError
                      : NameError
                      :TypeError
                      : ZeroDivisionError
                      : OSError
                      : AssertionError
"""

age = input("Quel âge as-tu ? ")

try:
    age = int(age)
except:
    print("l'âge est incorrect")
else:
    print("tu as",age,"ans .")
finally:
    print("fin du programme.")


print("\n")


nb = 150
nb2 = input("chosis un nombre plus petit ou égale à 150")

try:
    nb2 = int(nb2)
    print("rslt = {}".format(nb/nb2))
except ValueError:
    print("Vous devez entrer un nombre")
except ZeroDivisionError:
    print("Vous ne pouvez pas diviser par 0")
except:
    print("Valeur incorrecte")
else:
    print("c'est un bon choix")
finally:
    print("fin fu programme")


print("\n")


try:
    age = input("Quel âge as-tu ? ")
    age = int(age)

    assert age > 18 #je veux que l'âge soit plus grand que 18
except AssertionError:
    print("j'ai attrapé l'execption")