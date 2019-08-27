#coding:utf-8
#from random import randint
"""
Jeux du plus ou moins

Fais en sorte que le programme choisisse un nombre au hasard entre 0 et 1000 inclus 
et trouves-le en 8 chances.
lorsque que tu entres un nombre, fais en sorte que le programme te dise si le nombre à trouver 
est plus petit ou plus grand
Si tu ne l'as pas trouvé, retourne un game over 

print(value)
    if tresor < value:
        print("Nope.)
    elif tresor > value:
        print("Nope.)
    else:
        print("Congratulation! Computer: ".tresor.". You: ". value)


"""

from random import randrange
tresor = randrange(800)
tresor = int(tresor)
user = 8
user = int(user)
value = 0
while (user > 0) and (value != tresor):
    value = input("Guess a number between 0 and 800. You have "+format(user)+" chances to find the answer!")
    value = int(value)
    print(value)
    if tresor < value:
        user = user-1
        print("Nope. It's smaller than "+format(value)+". But you still have "+format(user)+" chances!")
    elif tresor > value:
        user = user-1
        print("Nope. It's higher than "+format(value)+". But you still have "+format(user)+" chances!")   
    else:
        print("Congratulation! Computer: "+format(tresor)+". You: "+format(value))
if user == 0:
    print("Sorry, you lost. The answer was: "+format(tresor))