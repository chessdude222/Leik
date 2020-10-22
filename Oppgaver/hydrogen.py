k_e = 9*10**9
e = 1.6*10**-19
G = 6.7*10**-11
m_p = 1.7*10**-27
m_e = 9.1*10**-31
r = 5.3*10**-11

c_force = k_e*e**2/r**2
g_force = G*m_p*m_e/r**2

print(f"The columb force is{c_force: .1e} kgm/s^2, the gravitational force is{g_force: .1e} kgm/s^2, the ratio is {c_force/g_force: g}")
