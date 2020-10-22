# Oppgave a
elements_10 = {1: '-', 2: 'Helium', 3: 'Lithium',
4: 'Beryllium', 5: 'Boron', 6: 'Carbon',
7: 'Nitrogen', 8: '-',
9: 'Fluorine', 10: 'Neon'}

elements_10[1] = 'Hydrogen'; elements_10[8] = 'Oxygen'

# Oppgave b
elements_10_copy = elements_10.copy()
elements_10_copy.update({11: 'Sodium'})
print(elements_10)
print('\n')
elements_11 = elements_10
elements_11.update({11: 'Sodium'})
print(elements_10)

'''
The first dictionary that is printed is just the original, with no modifications.
The second is a updated one with the eleventh element in the periodic table added.
They are different because even though we update elements_11 and not elements_10,
we are still referencing elements_10 when working with elements_11. This is because
elements_11 is just a reference to another dictionary, therefore when we update elements_11
we update elements_10 as well. Because elements_11 is exactly the same dictionary as elements_10.
'''


'''
terminal > python chemical_elements_dict.property.py
{1: 'Hydrogen', 2: 'Helium', 3: 'Lithium', 4: 'Beryllium', 5: 'Boron', 6: 'Carbon', 7: 'Nitrogen', 8: 'Oxygen', 9: 'Fluorine', 10: 'Neon'}


{1: 'Hydrogen', 2: 'Helium', 3: 'Lithium', 4: 'Beryllium', 5: 'Boron', 6: 'Carbon', 7: 'Nitrogen', 8: 'Oxygen', 9: 'Fluorine', 10: 'Neon', 11: 'Sodium'}
'''
