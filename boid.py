# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 10:26:59 2020

@author: Tobias
"""


import vector
import numpy as np

class boid:
    
    def __init__(self, x, y):
        self.position = vector.Vector(x,y)
        vec = (np.random.rand(2) - 0.5)*10
        self.velocity = vector.Vector(*vec)
              
def rule1(boid):
    
    pcj = vector.Vector(1,1)
    N = 1
    for b in flock:
        N += 1
        if b != boid:
            pcj = pcj - boid.position
    pcj = pcj / (N-1)
    
    return ((pcj-boid.position) / 100)

def rule2(boid):
    
    c = vector.Vector(1,1)
    
    for b in flock:
        if b != boid:
            if ((abs(b.position - boid.position)) < 100):
                c = c - (b.position - boid.position)                 
    return c

def rule3(boid):
    pvj = vector.Vector(1,1)
    N = 1
    for b in flock:
        N += 1
        if b != boid:
            pvj = pvj + b.velocity
            
    pvj = pvj / (N-1)
    return ((pvj - boid.velocity) / 8)                  
                
def move_all_boids_to_new_positions(boids):    
    for b in boids:
        v1 = rule1(b)
        v2 = rule2(b)
        v3 = rule3(b)
        
        b.velocity = b.velocity + v1 + v2 + v3
        b.position = b.position + b.velocity
        

flock = [boid(*np.random.rand(2)*1000) for _ in range(2)]

x = 0
number = 5

while x < number:
    move_all_boids_to_new_positions(flock)
    for boid in flock:
        print("boid x position = " + str(boid.position.x))
        print("boid y position = " + str(boid.position.y))
        print("boid x velocity = " + str(boid.velocity.x))
        print("boid y velocity = " + str(boid.velocity.y))
    x += 1



