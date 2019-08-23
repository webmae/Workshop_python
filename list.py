ma_list = [1,2,3,4,5,6,7,8,9,'chat','chien','cochon']
print ma_list
ma_list.remove('chat')
print ma_list
ma_list.insert(0,'Hey la-bas cow-boy')
print ma_list
print len(ma_list)

new_list = ma_list[:]

new_list[new_list.index('chien')] = 'vache'
print new_list
print ma_list