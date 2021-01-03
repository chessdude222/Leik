class RungeKutta2(ForwardEuler):
    def solve(self):
        for k in range(len(self.t)-1):
            self.dt = self.t[i+1] - self.t[i]
            self.u[u+1] = self.advance()
        return self.t, self.u

    def advance(self):
        u, t, dt = self.u, self.t, self.dt
        K1 = dt*f(u[k], t[k])
        K2 = dt*f(u[k] + 0.5*K1, t[k] + 0.5*dt)
        return u[k] + K2
