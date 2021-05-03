from vpython import *

from planet import Planet

G = 100

# earth moon sun
planet1 = Planet(1, 1 / 10, (-72.0, 0, 0), (0, -1, 0))
planet2 = Planet(5, 1, (-80, 0, 0), (0, -6, 0))
planet3 = Planet(10, 30, (0, 0, 0), (0, 0, 0))

# creating orbs
orb1 = sphere(pos=vector(planet1.position_x, planet1.position_y, planet1.position_z), radius=planet1.radius,
              color=color.yellow)
orb2 = sphere(pos=vector(planet2.position_x, planet2.position_y, planet2.position_z), radius=planet2.radius,
              color=color.orange)
orb3 = sphere(pos=vector(planet3.position_x, planet3.position_y, planet3.position_z), radius=planet3.radius,
              color=color.cyan)

orb1.m = planet1.mass
orb2.m = planet2.mass
orb3.m = planet3.mass

orb1.p = vector(planet1.momentum_x, planet1.momentum_y, planet1.momentum_z)
orb2.p = vector(planet2.momentum_x, planet2.momentum_y, planet2.momentum_z)
orb3.p = vector(planet3.momentum_x, planet3.momentum_y, planet3.momentum_z)

attach_trail(orb1)
attach_trail(orb2)
attach_trail(orb3)

t = 0
dt = 0.0005

while t < 1000:
    rate(10000)

    # vector from star 1 to 2
    vec12 = orb2.pos - orb1.pos
    vec21 = -vec12

    # vector from star 1 to planet
    vec13 = orb3.pos - orb1.pos
    vec31 = -vec13

    # vector from star 2 to planet
    vec23 = orb3.pos - orb2.pos
    vec32 = -vec23

    # calculate grav force on star 1 due to 2
    F12 = -G * orb1.m * orb2.m * norm(vec12) / mag(vec12) ** 2
    F21 = -G * orb1.m * orb2.m * norm(vec21) / mag(vec21) ** 2
    # calculate the force on planet due to star 1
    F13 = -G * orb1.m * orb3.m * norm(vec13) / mag(vec13) ** 2
    F31 = -G * orb1.m * orb3.m * norm(vec31) / mag(vec31) ** 2
    # calculate the force on planet due to star 2
    F23 = -G * orb2.m * orb3.m * norm(vec23) / mag(vec23) ** 2
    F32 = -G * orb2.m * orb3.m * norm(vec32) / mag(vec32) ** 2

    # update momentum (with total vector force)
    orb1.p = orb1.p + (F21 + F31) * dt
    orb2.p = orb2.p + (F12 + F32) * dt
    orb3.p = orb3.p + (F13 + F23) * dt

    # update position
    orb1.pos = orb1.pos + orb1.p * dt / orb1.m
    orb2.pos = orb2.pos + orb2.p * dt / orb2.m
    orb3.pos = orb3.pos + orb3.p * dt / orb3.m

    t = t + dt
