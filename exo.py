print('quel est ton age?')
age = input()
if (age < 18) or (age > 65):
    print("Tu ne peux pas passer ton permis")
else:
    print("Tu peux passer ton permis")

i = 1
while i < 10:
  print("j'adore le python")
  i += 1

i = 0
mot = "banana"
for x in mot:
  i+=1
print (mot+ " contient {} lettres.".format(i))