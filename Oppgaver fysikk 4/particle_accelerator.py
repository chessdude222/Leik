import sys
#m_e = 9.1*10**-31
#q = 1.6*10**-19
E = 0.02

try:
    v_0 = sys.argv[1]
    #input("enter v0 :")

    t = sys.argv[2]
    #input("enter t: ")

    q = sys.argv[3]

    m = sys.argv[4]
except:
    print("Too few arguments")
    exit()

try:
    v_0 = float(v_0)
    m = float(m)
    q = float(q)
    t = float(t)
except:
    print("Input needs to be a number")
    exit()

try:
    x = v_0*t + 0.5*q*E*(t**2)/m
    v = v_0 + q*E*t/m
except:
    print("Too few inputs")
    exit()

print(f"x(t) = {x}, v(t) = {v}")
