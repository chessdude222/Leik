def read_file(filename):
    dict = {}
    with open(filename, 'r') as infile:
        for line in infile:
            name = line.split()
            name1 = ''
            for i in name[1:]:
                name1 += ' ' + i
            name1 = name1.strip()
            dict[name[0]] = name1
    return dict

print(read_file('test.txt'))
