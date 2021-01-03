def sum_file(inputname, outputname):
    with open(inputname, 'r') as infile:
        lines = []
        sum = []
        for line in infile:
            numbers = line.split()
            s = 0
            for i in numbers:
                s += float(i)
            sum.append(s)
            lines.append(numbers)

    with open(outputname, 'w') as outfile:
        for i in range(len(lines)):
            for n in lines[i]:
                n = float(n)
                outfile.write(f'{n:3.2f}  ')
            outfile.write(f'{sum[i]:3.2f}\n')

sum_file('numbers.txt', 'out.txt')
