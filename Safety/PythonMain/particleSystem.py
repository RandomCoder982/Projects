#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, random, math, time, sys
import numpy as np
 
# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()

pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500),0,32)

particles = []
gravity = 0.1
xVelocity = 0.01
yVelocity = random.randint(0, 5)
particleSize = 20
colisionDamping = .7
lowerBoundx = 50
upperBoundx = 450
upperBoundy = 450
startx = 50
starty = 10
mouseClicked = False
mass = 1
 

clicking = False 

# Loop ------------------------------------------------------- #
while True:
    
    # Background --------------------------------------------- #
    screen.fill((0 , 0 , 0))
    mx, my = pygame.mouse.get_pos()
    pygame.draw.rect(screen, (0, 255, 0), (startx, starty, upperBoundx - startx, upperBoundy - starty), 1)
 
    # Particles ---------------------------------------------- #
    if clicking == True:
        clicking == False

    
 
    for particle in particles:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]

        gravitationalForce = particle[2] * gravity
        particle[1][1] += gravity * particle[2]
        pygame.draw.circle(screen, (0, 0, 255), [int(particle[0][0]), int(particle[0][1])], particleSize)

        if particle[0][1] > upperBoundy - particleSize:
            particle[1][1] *= -1 * colisionDamping
        
        if particle[0][0] < lowerBoundx + particleSize:
            particle[1][0] *= -1 * colisionDamping

        if particle[0][0] > upperBoundx - particleSize:
            particle[1][0] *= -1 * colisionDamping
    
    for particle_a in particles:
        for particle_b in particles:
            dx = particle_a[0][0] - particle_b[0][0]
            dy = particle_a[0][1] - particle_b[0][1]

            distance = math.sqrt(dx * dx + dy * dy)

            if 0 < distance < 2 * particleSize:
                total_mass = particle_a[2] + particle_b[2]
                particle_a[1] = (particle_a[2] * particle_a[1] + particle_b[2] * particle_b[1]) / total_mass
                particle_b[1] = particle_a[1]

                

            
            
        


    # Buttons ------------------------------------------------ #
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_w:
                particles.append([[random.randint(100, 400), random.randint(100, 400)], [xVelocity, yVelocity]])
            if event.key == K_s:
                particles.pop()
        
        if event.type == MOUSEBUTTONDOWN and not mouseClicked:
            mouseClicked = True
            Position = np.array([mx, my])
            Velocity = np.array([xVelocity, yVelocity])
            Mass = np.array(mass)
            particles.append([Position, Velocity, Mass])
        
        if event.type == MOUSEBUTTONUP:
            mouseClicked = False
        


 
#-------------------------- #
    pygame.display.update()
    mainClock.tick(60)