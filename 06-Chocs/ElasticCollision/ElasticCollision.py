# To start the simluation place the particles on the scene and press 'S' key.
# To pause the simulation and replace particles press 'R' key

import numpy as np
mass = lambda density, radius : (4 / 3) * density * np.pi * radius ** 3

# Pre-defined initial constant parameters for the environment

# particle's speed]
v1, v2 = 150.0, 150.0

# particle's radius
RADIUS = 30

# density should vary from 0 to 127 (due to color settings)
DENSITY1, DENSITY2  = 70, 70

MASS1, MASS2 = mass(DENSITY1, RADIUS), mass(DENSITY2, RADIUS)
print('Mass1: Mass2: {}, {}'.format(MASS1, MASS2))
# intial partice's position,speed and acceleration
X1_INITIAL, X2_INITIAL = [[0.0, 0.0]], [[100.0, 100.0]]
V_INITIAL = [[0.0, 0.0]]
V_START = [[0.0, 0.0]]

A_INITIAL = np.asarray([0, 0])
# screen dimensions
DIM = np.asarray([600, 600])

GRAVITY = np.asarray([0, 0])
dt = 0.01

import numpy as np
import pygame as pg
import math
from pygame.locals import *

import pygame
import pygame.gfxdraw
import numpy as np

from Environment import Environment
from Particle import Particle

def display(env):
    for p in env.particles:
        pygame.gfxdraw.filled_circle(screen, int(p.X[0][0]), int(p.X[0][1]), p.radius, p.colour)

def findParticle(particles, x, y):

    for p in particles:
        if math.hypot(p.X[0][0]-x, p.X[0][1]-y) <= p.radius:
            return p
    return None


def findParticleById(particles, particle_id):

    for p in particles:
        if p.id == particle_id:
            return p
    return None

# Code is based on https://github.com/seanny1986/particlePhysics

env = Environment(DIM, GRAVITY, dt)

pygame.init()

screen = pygame.display.set_mode((DIM[0], DIM[1]))
pygame.display.set_caption('Elastic Collision Simulation')

particles = []

env = Environment(DIM, GRAVITY, dt)

widgets = []


def textbox_callback(id, final):
    print('enter pressed, textbox contains {}'.format(final))


entry_settings = {
    "inactive_on_enter": False,
    'active': False
}

pygame.init()

screen = pygame.display.set_mode((DIM[0], DIM[1]))
pygame.display.set_caption('Elastic Collision Simulation')

particles = []

# intial control parameters
running, intro, set_initial_parameters, circle_draging, direction_dragging = True, True, True, False, False
selected_particle = None

# simluation start
while running:

    if intro:

        screen.fill([255, 255, 255])
        env.update()
        display(env)
        events = pygame.event.get()

        pygame.display.flip()
        mx, my = pygame.mouse.get_pos()

        # initialize particles on the scene

        if set_initial_parameters:
            particle1 = Particle(1, env, X1_INITIAL, V_INITIAL, V_START, A_INITIAL, RADIUS, MASS1, DENSITY1)
            particle2 = Particle(2, env, X2_INITIAL, V_INITIAL, V_START, A_INITIAL, RADIUS, MASS2, DENSITY2)

            particles.append(particle1), particles.append(particle2)
            env.addParticle(particle1), env.addParticle(particle2)

            set_initial_parameters = False

        # Reset initial positions of the particles on the scene, control the beginning of the simulation
        for w in widgets:
            w.update()
            w.draw(screen)
        pg.display.update()

        if direction_dragging == True:

            if current_selected_particles is not None:
                x, y = current_selected_particles.X[0][0], current_selected_particles.X[0][1]
                mx, my = pygame.mouse.get_pos()
                slope = (y - my) / (x - mx + 0.1)
                DISPLAY_WIDTH = 640

                x_new = DISPLAY_WIDTH if x < mx else -DISPLAY_WIDTH
                y_new = y + slope * (x_new - x)
                pygame.draw.line(screen, (0, 0, 0), (x, y), (x_new, y_new), 2)
                pg.display.update()

        for event in pygame.event.get():

            for w in widgets:
                w.get_event(event)

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                selected_particle = findParticle(particles, mouseX, mouseY)
                if selected_particle is not None:
                    selected_particle.colour = (255, 0, 0)

                if selected_particle:

                    circle_draging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = selected_particle.X[0][0] - mouse_x
                    offset_y = selected_particle.X[0][1] - mouse_y

            elif event.type == pygame.MOUSEBUTTONUP:
                circle_draging = False

                if selected_particle is not None and direction_dragging == False:
                    direction_dragging = True
                    current_selected_particles = selected_particle

                elif direction_dragging:

                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    rel_x, rel_y = mouse_x - current_selected_particles.X[0][0], mouse_y - current_selected_particles.X[0][1]
                    angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
                    x_velocity = v1*math.cos(-angle*np.pi/180)
                    y_velocity = v1*math.sin(-angle*np.pi/180)

                    selected_particle = findParticleById(particles, current_selected_particles.id)
                    selected_particle.V_start = [[x_velocity, y_velocity]]

                    direction_dragging = False
                    current_selected_particles.colour = current_selected_particles.base_colour
                    current_selected_particles = None

            elif event.type == pygame.MOUSEMOTION:
                if circle_draging:
                    mouse_x, mouse_y = event.pos
                    selected_particle.X[0][0] = mouse_x + offset_x
                    selected_particle.X[0][1] = mouse_y + offset_y

            elif event.type == KEYDOWN:

                if event.key == pygame.K_s:
                    for p in env.particles:
                        p.V = p.V_start

                    intro = False
    else:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == KEYDOWN:

                if event.key == pygame.K_r:
                    env.particles[0].X, env.particles[1].X = X1_INITIAL, X2_INITIAL
                    env.particles[0].V, env.particles[1].V = V_INITIAL, V_INITIAL
                    env.particles[0].A, env.particles[1].A = A_INITIAL, A_INITIAL

                    intro = True

        screen.fill([255, 255, 255])
        env.update()
        display(env)
        pygame.display.flip()