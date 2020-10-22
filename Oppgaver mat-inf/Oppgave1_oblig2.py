# oppgave 1
# f'(a) = (f(a+h) - f(a-h))/2
# t_i er en liste med verdier for tid (x-verdier)
# v_i er en liste med verdier for fart (y-verdier)
# a = (v_2 - v_1)/(t_2 - t_1)


t_i = []
v_i = []
infile = open('running.txt','r')
for line in infile:
 tnext, vnext = line.strip().split(',')
 t_i.append(float(tnext))
 v_i.append(float(vnext))
infile.close()

def a(t):
    for i in range(len(t_i)):
        if t >= t_i[i] and t <= t_i[i+1]:
            s = i
            break
    a = (v_i[s+1] - v_i[s])/(t_i[s+1]-t_i[s])
    return a


def s(t):
    for i in range(len(t_i)):
        if t >= t_i[i] and t <= t_i[i+1]:
            s = i
            break
    sum = 0
    for n in range(s):
        a = (v_i[n+1] - v_i[n])/(t_i[n+1]-t_i[n])
        sum += v_i[n]*(t_i[n+1] - t_i[n]) + 0.5*a*(t_i[n+1] - t_i[n])**2
    t_extra = t - t_i[s]
    sum += v_i[s]*t_extra
    return sum


import numpy as np
import matplotlib.pyplot as plt

a_vectorized = np.vectorize(a)
t_values = np.linspace(t_i[0], t_i[-1], 20000)
a_values = a_vectorized(t_values)
plt.plot(t_values, a_values, 'midnightblue')
plt.grid()
plt.xlabel('t_values')
plt.ylabel('acceleration')
plt.show()

s_vectorized = np.vectorize(s)
s_values = s_vectorized(t_values)
plt.plot(t_values, s_values, 'midnightblue', label ='distance')
plt.grid()
plt.xlabel('t-values')
plt.ylabel('distance')
plt.show()

print(s(t_i[-1]))
