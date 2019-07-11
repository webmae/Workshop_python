#coding::utf-8

"""
Propriété : manière de manipuler/controler des attributs
          : principe d'encapsulation
"""

class Humain():
    """cette classe représente un humain"""

    def __init__(self,nom, age):
        print("creation d'un humain")
        self.nom = nom
        self._age = age


    def _getage(self):
        try:
            return self._age
        except:
            print("l'age n'existe pas")

    def _setage(self,nouvel_age):
        if nouvel_age < 0:
            self._age = 0
        else:
            self._age = nouvel_age


    def _delage(self):
        del self._age
        
    #property(<getter>, <setter>, <deleter>, <helper>)
    age = property(_getage,_setage,_delage,"je suis l'age d'un humain") #sans ces propriétés, ca ne fonctionne pas

#programme principale
h1 = Humain("perry",22)
h1.age = 14
print("tues {} et tu as {}".format(h1.nom,h1.age))

print("\n")


print(h1.age)

h1.age = -5

#del  est un mot reserver qui modifie un attribut d'une instance
del h1.age

print(h1.age)

print('\n')

help(Humain)
print('\n')
print('\n')

help(Humain.age)

