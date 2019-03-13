class Particle():

    def __init__(self, id, env, X, V, V_start, A, radius, mass, density):

        self.env = env
        self.id = id
        self.X = X
        self.V = V
        self.V_start = V_start
        self.A = A
        self.radius = radius
        self.mass = mass
        self.density = density
        self.colour = (0, 0, 255-density*2)
        self.base_colour = self.colour

    def addForce(self, F):

        self.A += F / self.mass

    def addAcceleration(self, acc):

        self.A += acc

    def addVelocity(self, vel):

        self.V += vel

    def addPosition(self, pos):

        self.X += pos

    def attract(self, particle):

        r = self.X - particle.X
        self.A += 6.67408e-11 * particle.mass / r ** 2

    def stateUpdate(self):

        self.V += self.A * self.env.dt
        self.X += self.V * self.env.dt - 0.5 * self.A * self.env.dt ** 2