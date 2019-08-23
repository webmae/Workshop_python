#!/bin/bash
print("hello world")

def dire_bonjour (nom,message):
        print(" {} dit {}. ".format(nom,message))
        
dire_bonjour("perry","salut ca va ?")

print ("beau perry")

coucou = "coucou"
comment = "comment"
cava = "ca va"
espace = "\n"


print (coucou+espace+comment+espace+cava)

print('quel est ton age?')
age = input('')
print('Tu as {} ans !'.format(age)) 

nombre = 34
nom = "loulou"

print(type(nombre))
print(type(nom))

print (nom + " a {} ans".format(nombre))