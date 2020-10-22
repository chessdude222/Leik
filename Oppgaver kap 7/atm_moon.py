def moonreader(filename):
    with open (filename, 'r') as infile:
        dict = {}                       # Makes the dictionary that values will be stored in
        infile.readline()
        for line in infile:
            values = line.split(';')    # Split the name and number values up
            for i in range(len(values)):
                name, value = values[i].split('-')  # Splits the name and value
                name = name.strip()                 # Takes away white spaces in the name
                name = name.upper()                 # Makes the name upper case
                value = value.strip()
                if ',' in value:                    # Removes the comma in the values
                    value = value.replace(',','')
                value = float(value)
                dict[name] = value                  # Fills in the pairs in the dictionary
    return dict

dict = moonreader('atm_moon.txt')
print(dict['NEON 20']) # Example from the book
print(dict)
'''
terminal > atm_moon.py
40000.0
'''
