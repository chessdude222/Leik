# Oppgave a
def read_person_data(filename):
    dict = {}
    with open(filename, 'r') as infile:
        for line in infile:
            info = line.split(',')          # Splits the line into the three values we want
            for i in range(len(info)):
                info[i] = info[i].strip()   # Makes the values be in the desired format
            temp = {'Age': float(info[1]), 'Gender': info[2]} # Makes the dictionary that's going to be nested
            dict[info[0]] = temp
    return dict

# Oppgave b
def write_person_data(data_dict, filename):
    with open(filename, 'w') as outfile:
        for i in data_dict: # Writes to the document by looping through the keys, and then indexing
            outfile.write(f"{i}, {data_dict[i]['Age']}, {data_dict[i]['Gender']}\n")


dict = read_person_data('name_data.txt')    # Creates the dictionary
write_person_data(dict, 'names.txt')        # Runs the function and we get the text file
print(dict)

"""
Terminal > people_dict.py
(Putter tekstfilen i devilry)
"""
