from boid import *
from random import randint
import random
import numpy as np

class World(object):

    def __init__(self, width, height, numBoids, boidConfig):
        random.seed(1)
        self.boids = self.CreateBoids(width, height, numBoids, boidConfig)
        self._numBoids = numBoids
        self._colourList = [[255,0,0], [0,255,0], [0,0,255], [255,255,0], [255,0,255], [0,255,255], [255,127,0], [127,255,0], [127,0,255], [255,0,127], [0,127,255], [0,255,127], [127,0,0], [0,127,0], [0,0,127], [127,127,0], [127,0,127], [0,127,127], [127,127,127], [63,127,0], [63,0,127], [0,63,127], [127,63,0], [127,0,63], [0,127,63], [190,127,0], [190,0,127], [0,190,127], [127,190,0], [127,0,190], [0,127,190], [190,63,0], [190,0,63], [0,190,63], [63,190,0], [63,0,190], [0,63,190], [63,255,0], [63,0,255], [0,63,255], [255,63,0], [255,0,63], [0,255,63], [190,255,0], [190,0,255], [0,190,255], [255,190,0], [255,0,190], [0,255,190], [64,64,64], [190,190,190], [127,127,127], [255,0,0], [0,255,0], [0,0,255], [255,255,0], [255,0,255], [0,255,255], [255,127,0], [127,255,0], [127,0,255], [255,0,127], [0,127,255], [0,255,127], [127,0,0], [0,127,0], [0,0,127], [255,0,0], [0,255,0], [0,0,255], [255,255,0], [255,0,255], [0,255,255], [255,127,0], [127,255,0], [127,0,255], [255,0,127], [0,127,255], [0,255,127], [127,0,0], [0,127,0], [0,0,127], [127,127,0], [127,0,127], [0,127,127], [127,127,127], [63,127,0], [63,0,127], [0,63,127], [127,63,0], [127,0,63], [0,127,63], [190,127,0], [190,0,127], [0,190,127], [127,190,0], [127,0,190], [0,127,190], [190,63,0], [190,0,63], [0,190,63], [63,190,0], [63,0,190], [0,63,190], [63,255,0], [63,0,255], [0,63,255], [255,63,0], [255,0,63], [0,255,63], [190,255,0], [190,0,255], [0,190,255], [255,190,0], [255,0,190], [0,255,190], [64,64,64], [190,190,190], [127,127,127], [255,0,0], [0,255,0], [0,0,255], [255,255,0], [255,0,255], [0,255,255], [255,127,0], [127,255,0], [127,0,255], [255,0,127], [0,127,255], [0,255,127], [127,0,0], [0,127,0], [0,0,127], [255,255,255]]
        self.count = 0
        self.updateGroups = 1
        self.boidConfig = boidConfig
        self.width = width
        self.height = height

    def updateLocalBoids(self):
        print("reached")
            
    def updateBoidPos(self, dt):
        for i in range(0, len(self.boids)):
            self.boids[i].updatePos(dt, self.boids)

    def CreateBoids(self, width, height, num, boidConfig):
        boids = []
        for i in range(num):
            x = randint(boidConfig[6],boidConfig[7])
            if randint(0,1) == 1:
                x = -x
            y = randint(boidConfig[6],boidConfig[7])
            if randint(0,1) == 1:
                y = -y
            #boids.append(Boid([randint(0,width), randint(0,height)], [width,height], [x, y], [255, 255, 255], num, boidConfig))
            boids.append(Boid([width/2, height/2], [width,height], [x, y], [255, 255, 255], num, boidConfig))
        return boids

    def getVetexBatch(self):
        batch = []
        for b in self.boids:
            batch.append(b.getVertexList())
        return batch

    def getColourBatch(self):
        batch = []
        for b in self.boids:
            batch.append(b._colour)
        return batch

    def getLocationBatch(self, boids):
        batch = []
        for b in boids:
            batch.append(b._position)
        return batch
        