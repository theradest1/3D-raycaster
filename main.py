import numpy
import time

FOV = 10
mapSize = (3,3,3)
map = numpy.array([[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0]]])

def cast(x,y,z):
  for in range(FOV):
    
x, y, z = mapSize
while True:
  cast(x, y, z)