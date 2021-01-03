import matplotlib.pyplot as plt
from ODEsolver import *

# Oppgave a
class Region:
    def __init__(self, name, S_0, E2_0):
        # Initalises the inital conditions for the individual Region
        self.name = name
        self.S0 = S_0
        self.E2_0 = E2_0
        self.E1_0 = 0
        self.I0 = 0
        self.Ia_0 = 0
        self.R_0 = 0
        self.population = S_0 + E2_0

    def set_SEIR_values(self, u, t):
        # Function to assign calulated values to the class
        self.S = u[:,0]; self.E1 = u[:,1]
        self.E2 = u[:,2]; self.I = u[:,3]
        self.Ia = u[:,4]; self.R = u[:,5]
        self.t = t

    def plot(self):
        # Gets the desired values and plots them
        S, I, Ia, R, t = self.S, self.I, self.Ia, self.R, self.t
        plt.xlabel('Time(days)')
        plt.ylabel('Population')
        plt.title(f'{self.name}')
        plt.plot(t, S, 'midnightblue', label = 'Suspectible')
        plt.plot(t, I, 'orange', label = 'Symptomatic infected')
        plt.plot(t, Ia, 'g', label = 'Asymptomatic infected')
        plt.plot(t, R, 'r',label = 'Recovered')

if __name__ == '__main__':
    nor = Region('Norway',S_0=5e6,E2_0=100)

    print(nor.name, nor.population)
    S_0, E1_0, E2_0 = nor.S0, nor.E1_0, nor.E2_0
    I_0, Ia_0, R_0 = nor.I0, nor.Ia_0, nor.R_0
    print(f'S_0 = {S_0}, E1_0 = {E1_0}, E2_0 = {E2_0}')
    print(f'I_0 = {I_0}, Ia_0 = {Ia_0}, R_0 = {R_0}')
    u = np.zeros((2,6))
    u[0,:] = [S_0, E1_0, E2_0, I_0, Ia_0, R_0]
    nor.set_SEIR_values(u,0)
    print(nor.S, nor.E1, nor.E2, nor.I, nor.Ia, nor.R)

# Oppgave b
class ProblemSEIR:
    def __init__(self, region, beta, r_ia = 0.1, r_e2=1.25, lmbda_1=0.33, lmbda_2=0.5, p_a=0.4, mu=0.2):
        # Checks if beta is constant or dependent on t
        if isinstance(beta, (float, int)):
            self.beta = lambda t: beta
        elif callable(beta):
            self.beta = beta

        self.region = region
        self.r_ia = r_ia
        self.r_e2 = r_e2
        self.lmbda_1 = lmbda_1
        self.lmbda_2 = lmbda_2
        self.p_a = p_a
        self.mu = mu

        # Sets the inital conditions by using a defined function
        self.set_initial_condition()

    def set_initial_condition(self):
        # Takes the intial values from the region in constructor and makes them
        # a part of ProblemSEIR as self.inital_condition
        reg = self.region
        self.initial_condition = [reg.S0, reg.E1_0, reg.E2_0, reg.I0, reg.Ia_0, reg.R_0]


    def get_population(self):
        # Gets the population from the region in the constructor
        return self.region.population

    def solution(self, u, t):
        return self.region.set_SEIR_values(u, t)

    def __call__(self, u, t):
        beta = self.beta; r_ia = self.r_ia; r_e2 = self.r_e2
        lmbda_1 = self.lmbda_1; lmbda_2 = self.lmbda_2; p_a = self.p_a; mu = self.mu

        S, E1, E2, I, Ia, R = u
        N = sum(u) # Calulates the population
        # Calulates the derivative values, and returns them as a list
        dS = -beta(t)*S*I/N - r_ia*beta(t)*S*Ia/N - r_e2*beta(t)*S*E2/N
        dE1 = beta(t)*S*I/N + r_ia*beta(t)*S*Ia/N + r_e2*beta(t)*S*E2/N - lmbda_1*E1
        dE2 = lmbda_1*(1-p_a)*E1 - lmbda_2*E2
        dI = lmbda_2*E2 - mu*I
        dIa = lmbda_1*p_a*E1 - mu*Ia
        dR = mu*(I + Ia)
        return [dS, dE1, dE2, dI, dIa, dR]

if __name__ == '__main__':  # Makes it possible to import from file
    problem = ProblemSEIR(nor,beta=0.5)
    problem.set_initial_condition()
    print(problem.initial_condition)
    print(problem.get_population())
    print(problem([1,1,1,1,1,1],0))

# Oppgave c
class SolverSEIR:
    def __init__(self, problem, T, dt):
        # Initalises the values needed to solve the ODE
        self.problem = problem
        self.T = T
        self.dt = dt
        self.total_population = problem.get_population()

    def solve(self, method=RungeKutta4):
        # Solves the ODE and puts the values back in the ProblemSEIR class
        solver = method(self.problem)
        solver.set_initial_condition(self.problem.initial_condition)
        points = int(self.T*self.dt + 1)   # Includes the first value, so need to add one
        t = np.linspace(0, self.T, points)
        u, t = solver.solve(t)
        self.problem.solution(u, t)

if __name__ == '__main__':  # Makes it possible to import from file
    solver = SolverSEIR(problem,T=100,dt=1.0)
    solver.solve()
    nor.plot()
    plt.legend()
    plt.show()

"""
Terminal > python SEIR.py
Norway 5000100.0
S_0 = 5000000.0, E1_0 = 0, E2_0 = 100 I_0 = 0, Ia_0 = 0, R_0 = 0
[5000000.       0.] [0. 0.] [100.   0.] [0. 0.] [0. 0.] [0. 0.]
[5000000.0, 0, 100, 0, 0, 0]
5000100.0
[-0.19583333333333333, -0.13416666666666668, -0.302, 0.3, -0.068, 0.4]
(shows a graph)
"""
