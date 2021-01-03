    from ODEsolver import *
import matplotlib.pyplot as plt

# Oppgave a
def SEIR(u,t):
    # Defines the parameters
    beta = 0.5; r_ia = 0.1; r_e2=1.25
    lmbda_1=0.33; lmbda_2=0.5; p_a=0.4; mu=0.2

    S, E1, E2, I, Ia, R = u
    N = sum(u)  # Calulates total population
    # Calulates the derivative
    dS = -beta*S*I/N - r_ia*beta*S*Ia/N - r_e2*beta*S*E2/N
    dE1 = beta*S*I/N + r_ia*beta*S*Ia/N + r_e2*beta*S*E2/N - lmbda_1*E1
    dE2 = lmbda_1*(1-p_a)*E1 - lmbda_2*E2
    dI = lmbda_2*E2 - mu*I
    dIa = lmbda_1*p_a*E1 - mu*Ia
    dR = mu*(I + Ia)
    # Returns a list with the calulated derivative values
    return [dS, dE1, dE2, dI, dIa, dR]

def test_SEIR():
    t = 0
    u = [1,1,1,1,1,1]
    expected = [-0.19583333333333333, -0.13416666666666668, -0.302, 0.3, -0.068, 0.4]
    computed = SEIR(u,t)
    tol = 1e-10
    for i in range(len(expected)):
        # Loops through computed and expected, and checks that the values are within the tol of each other
        msg = f'expected{expected[i]}, computed{computed[i]} for {i+1}th element'
        assert abs(expected[i]-computed[i]) < tol, msg

test_SEIR() # Calls the test function

# Oppgave b
def solve_SEIR(T, dt, S_0, E2_0):
    initial = [S_0, 0, E2_0, 0, 0, 0]       # Defines inital conditions
    points = int(T*dt + 1)                  # Start at 0 so needs to add a extra point
    timepoints = np.linspace(0, T, points)  # Calulates the time points for the ODE
    solution = RungeKutta4(SEIR)            # Initialises the ODEsolver
    solution.set_initial_condition(initial) # Sets the inital conditions for the ODEsolver
    u, t = solution.solve(timepoints)       # Computes the solution for the given time points
    return u, t

# Oppgave c
def plot_SEIR(u,t):
    # Indexes the values we want to plot from the solution
    S = u[:,0]
    I = u[:,3]
    Ia = u[:,4]
    R = u[:,5]
    # Plots the values
    plt.plot(t, S, 'midnightblue', label = 'S')
    plt.plot(t, I, 'orange', label = 'I')
    plt.plot(t, Ia, 'g', label = 'Ia')
    plt.plot(t, R, 'r', label = 'R')
    plt.legend()
    plt.show()

# Oppgave d

# Sets inital conditions and plots
S_0 = 5e6; E2_0 = 100; T = 100; dt = 1.0
u, t = solve_SEIR(T, dt, S_0, E2_0)
plot_SEIR(u,t)

"""
Terminal > python seir_func.py
(shows a graph)
"""
