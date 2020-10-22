from random import uniform

def filereader(filename):
    with open(filename, 'r') as infile:
        x = infile.readline()
        N = infile.readline()
    x = x.split()
    N = N.split()
    x = x[1:]
    N = N[1:]
    return x, N

def test_filereader():
    x_test = []
    N_test = []
    with open('test.txt', 'w') as outfile:
        outfile.write("x: ")
        for i in range(3):
            a = str(uniform(0.5, 1.5))
            outfile.write(a)
            x_test.append(a)
            outfile.write(" ")
        outfile.write("\n N: ")
        for n in range(15):
            b = str(uniform(10, 10000))
            outfile.write(b)
            N_test.append(b)
            outfile.write(" ")
    x, N = filereader('test.txt')
    success = x == x_test and N == N_test
    assert success

test_filereader()
