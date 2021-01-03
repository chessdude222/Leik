import numpy as np

def dump_data(filename, x, y, uncertainty):
    with open(filename, 'w') as outfile:
        for x_,y_,u_ in (x,y, uncertainty):
            outfile.write(f'{x_:.6f} {y_:e}')
            if u_ is not None:
                outfile.write(f'{u_:2.4f}')
            outfile.write('\n')
