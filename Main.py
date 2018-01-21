from vpython import *

# constants
R1 = 1
R2 = 1
R3 = 1
M1 = 1
M2 = 1
M3 = 1 / 10
G = 100

# creating the stars
planet1 = sphere(pos=vector(4.5, 0, 0), radius=R1, color=color.yellow)
planet2 = sphere(pos=vector(-4.5, 0, 0), radius=R2, color=color.orange)
planet3 = sphere(pos=vector(-10, 0, 0), radius=R3, color=color.cyan)

planet1.m = M1
planet2.m = M2
planet3.m = M3

planet1.p = vector(0, 2, 0)
planet2.p = vector(0, -3, 0)
planet3.p = vector(0, 0.1, 0)

attach_trail(planet1)
attach_trail(planet2)
attach_trail(planet3)


t = 0
dt = 0.0005

while t < 150:
    rate(10000)

    # vector from star 1 to 2
    vec12 = planet2.pos - planet1.pos
    vec21 = -vec12

    # vector from star 1 to planet
    vec13 = planet3.pos - planet1.pos
    vec31 = -vec13

    # vector from star 2 to planet
    vec23 = planet3.pos - planet2.pos
    vec32 = -vec23

    # calculate grav force on star 1 due to 2
    F12 = -G * planet1.m * planet2.m * norm(vec12) / mag(vec12) ** 2
    F21 = -G * planet1.m * planet2.m * norm(vec21) / mag(vec21) ** 2
    # calculate the force on planet due to star 1
    F13 = -G * planet1.m * planet3.m * norm(vec13) / mag(vec13) ** 2
    F31 = -G * planet1.m * planet3.m * norm(vec31) / mag(vec31) ** 2
    # calculate the force on planet due to star 2
    F23 = -G * planet2.m * planet3.m * norm(vec23) / mag(vec23) ** 2
    F32 = -G * planet2.m * planet3.m * norm(vec32) / mag(vec32) ** 2

    # update momentum (with total vector force)
    planet1.p = planet1.p + (F21 + F31) * dt
    planet2.p = planet2.p + (F12 + F32) * dt
    planet3.p = planet3.p + (F13 + F23) * dt

    # update position
    planet1.pos = planet1.pos + planet1.p * dt / planet1.m
    planet2.pos = planet2.pos + planet2.p * dt / planet2.m
    planet3.pos = planet3.pos + planet3.p * dt / planet3.m

    t = t + dt
