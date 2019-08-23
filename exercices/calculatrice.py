# coding:utf-8

"""
Crée un programme qui ressemble à une calculatrice qui calcul deux paramètres
    - ce programme devra utiliser :  multiplication
                                  :  division
                                  :  addition
                                  :  soustraction        
                                  :  exposant ( doit afficher avec et sans les décimals)   
                                  :  modulo ( doit afficher avec et sans les décimals)


Une fois ce petit programme réussi, essaie d'entrer un calcul (ex : 3 + 7 *5) et affiche la réponse

"""

def calcul():
    x = input("Enter a number")
    x = int(x)
    y = input("Enter an other number")
    y = int(y)
    operator = input("Please choose and type 'addition', 'division', 'multiplication', 'soustraction', 'modulo', 'exposant'!")
    str(operator)
    if operator == 'addition':
        solution = x + y
    elif operator == 'soustraction':
        solution = x - y
    elif operator == 'multiplication':
        solution = x * y
    elif operator == 'division':
        solution = x / y
    elif operator == 'modulo':
        solution = x % y
    elif operator == 'exposant':
        solution = x ** y
    else:
        solution = "not a right operator"
    print(solution)

calcul()