phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}

print()
print('*****  start section 1 - print dictionary ********')
print()

#print(phonebook)




print()
print('*****  end section 1 ********')
print()







print()
print('*****  start section 2 - search dictionary ********')
print()

if 'Chris' in phonebook:
    print(phonebook ['Chris'])
else:
    print("Chris is not in the phonebook")



print()
print('*****  end section 2 ********')
print()







"""print()
print('*****  start section 3 - edit/append dictionary ********')
print()



phonebook['Chris'] = '555-9876'
phonebook['Joe'] = '555-7654'
print(phonebook)

print()
print('*****  end section 3 ********')
print()"""






print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()


#del phonebook['Chris']


print(phonebook)

num_items = len(phonebook)

print(num_items)

mydict = {}



print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys ********')
print()

for k in phonebook:
    print(k)

for k in phonebook:
    print(phonebook[k])



print()
print('*****  end section 5 ********')
print()






print()
print('*****  start section 6 - iterate through values  ********')
print()

for v in phonebook.values():
    print(v)


print()
print('*****  end section 6 ********')
print()








print()
print('*****  start section 7 - iterate through both key and value pair********')
print()

#when cycle through items it produces a tuple which is immuatable

for k, v in phonebook.items():
    print(k)
    print(v)


print()
print('*****  end section 7 ********')
print()








print()
print('*****  start section 8 - using random and converting to list ********')
print()




print()
print('*****  end section 8 ********')
print()








