class SEIR_model:
    def __init__(self, p, q, r, S0, I0, T):
        self.p = p
        self.r = r
        self.q = q
        self.U0 = [S0, I0, 0, 0]
        self.T = T

    def __call__(self, u, t):
        p, r, q = self.p, self.r, self.q
        S, E, I, R = u
        s_d = -p(t)*S*I
        e_d = p(t)*S*I - q*E
        i_d = q*E - r*I
        r_d = r*I
        return [s_d, e_d, i_d, r_d]
