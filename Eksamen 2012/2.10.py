from TimeIntegral import *
import numpy as np

class MonteCarlo(TimeIntegral):
    def initialize(self):
        self.t = np.linspace(0, self.T, self.n+1)
        h = self.T/float(self.n + 1)
        self.w = np.zeros(len(self.t)) + h

def test_MonteCarlo():
    G = lambda t: 2.5
    T = 10
    problem = MonteCarlo(G, T, 11)
    computed = problem.compute()
    expected = 25
    tol = 1E-8
    success = abs(computed - expected) < tol
    assert success

test_MonteCarlo()
