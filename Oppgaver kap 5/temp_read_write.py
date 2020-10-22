import numpy as np

def extract_data(filename):
    temperatures = []
    with open(filename, 'r') as infile:
        infile.readline() # Skips the first line, could not get your method to work
        # Stores all the temperatues in one list
        for line in infile:
            temp = line.split()
            temperatures = temperatures + temp
    # Converts all temperatures to float
    for i in range(len(temperatures)):
        temperatures[i] = float(temperatures[i])
    return temperatures


oct_1945 = extract_data('temp_oct_1945.txt')
values1 = np.array(oct_1945)                    # Creates an array for faster computing
average_1945 = np.mean(values1)
maximum_1945 = np.max(values1)
minimum_1945 = np.min(values1)
oct_2014 = extract_data('temp_oct_2014.txt')
values2 = np.array(oct_2014)                    # Creates an array for faster computing
average_2014 = np.mean(values2)
maximum_2014 = np.max(values2)
minimum_2014 = np.min(values2)

print(f'In 1945 the average temperature in celsius were {average_1945:.3f}, the maximum were {maximum_1945} and the minimum was {minimum_1945}')
print(f'In 2014 the average temperature in celsius were {average_2014:.3f}, the maximum were {maximum_2014} and the minimum was {minimum_2014}')


# Oppgave b
def write_formatting(filename, list1, list2):
    with open(filename, 'w') as outfile:
        # Loops through the values in both lists, and creates a new line after both values have been written.
        for i in range(len(list1)):
            outfile.write(f'{list1[i]:4} {list2[i]:5}\n')

write_formatting('temp_formatted.txt', oct_1945, oct_2014)


"""
Oppgave a:
terminal > python temp_read_write.py
In 1945 the average temperature in celsius were 6.506, the maximum were 11.6 and the minimum was 2.1
In 2014 the average temperature in celsius were 8.855, the maximum were 13.6 and the minimum was 2.3
Oppgave b:
terminal > python temp_read_write.py
 7.2   9.8
 8.1  11.6
 8.9  11.5
11.6  13.3
 7.7  12.6
 8.7  10.3
 6.9   7.5
 5.4   9.3
 8.8  10.3
 8.9  10.3
 3.7   8.4
 3.3   8.8
 5.2   5.0
 9.6   5.8
10.8   6.8
 5.0   2.3
 5.4   3.5
 9.5   7.9
 5.3  11.8
 5.8  10.7
 2.3   9.0
 4.1   5.8
 6.6   6.8
 8.2  11.7
 6.1  10.6
 8.9  11.7
 6.6  13.1
 4.1  13.6
 2.8   8.0
 2.1   3.5
 4.1   3.2
(The same as in the .txt file)
"""
