class Planet:
    radius = 0

    mass = 0

    position_x = 0
    position_y = 0
    position_z = 0

    momentum_x = 0
    momentum_y = 0
    momentum_z = 0

    def __init__(self, r, m, position, momentum):
        self.radius = r
        self.mass = m
        self.position_x = position[0]
        self.position_y = position[1]
        self.position_z = position[2]
        self.momentum_x = momentum[0]
        self.momentum_y = momentum[1]
        self.momentum_z = momentum[2]
