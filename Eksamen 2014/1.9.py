def dump(filename, t, S, I, R, V):
    with open(filename, 'w') as outfile:
        for i range(len(r)):
            outfile.write(f'{t[i]:5.3f}{S[i]:5.3f}{I[i]:5.3f}{R[i]:5.3f}{V[i]:5.3f}\n')
