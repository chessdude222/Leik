class TimeIntegral:
    """
    Compute an approximation to the integral of G(t)
    from 0 to T using a numerical integration rule
    with n+1 function evaluations.
    """
    def __init__(self, G, T, n):
        self.G = G
        self.T = T
        self.n = n
        self.initialize() # compute weights and points
    def initialize(self):
        """
        Compute weights self.w and points self.t
        as two arrays of length self.n+1.
        """
        raise NotImplementedError
    def compute(self):
        """Return the approximation of the integral."""
        s = 0
        for p in range(self.n+1):
            s += self.w[p]*self.G(self.t[p])
        return s
