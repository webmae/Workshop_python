ma_Chaine = "Bonjour, comment vas-tu ? Nous sommes le 12 juillet 2019"
print  ma_Chaine.find('a')

new_Chaine = ma_Chaine.replace("o", "a")
print(new_Chaine) 
new_Chaine = ma_Chaine.replace("a", "o")
print(new_Chaine) 

print new_Chaine.isalpha()

if ma_Chaine.find('sommes'):
    print 'sommes'
else:
    print "nope"

