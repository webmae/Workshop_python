#coding:utf-8

"""
Opétations : + (addition)
             - (soustraction)
             * (multiplication)
             / (division)
             % (modulo)  -> le reste d'une division


variable = variable + x  ==> variable+=x
variable = variable - x  ==> variable-=x
variable = variable * x  ==> variable*=x
variable = variable / x  ==> variable/=x
variable = variable % x  ==> variable%=x

"""
calcul = 5 / 2
print(type(calcul))
print(calcul)
calcul = int(calcul)
print(type(calcul))
print(calcul)

calcul_deux = 15 % 2
print("le reste de calcul_deux est : ",calcul_deux)
calcul_deux = 14 % 2 
print("reste = {} car 2*7 = 14".format(calcul_deux))#le modulo peut servir a vérifier si un nombre est pair ou impair

print("\n")

calcul_trois = 5 + 3* 7
print("calcul_trois = {} car on suit les propriétés d'opérations".format(calcul_trois))
print('\n')

PersonnageLvl = input("quel est ton niveau ?")
PersonnageLvl = int(PersonnageLvl)

print("ton niveau est égale à",PersonnageLvl)
print("tu as gagné un lvl")
PersonnageLvl+=1
print("ton niveau est égale à",PersonnageLvl)