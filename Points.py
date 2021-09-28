import random
import math

def circle(numOfPoints):
    p = []
    half = numOfPoints/2
    radius = half
    center = (half,half)
    for i in range(numOfPoints):
        r = radius * math.sqrt(random.random())
        theta = random.random() * 2 * math.pi
        x = round(center[0] + r * math.cos(theta), 1)
        y = round(center[1] + r * math.sin(theta), 1)
        p.append((x,y))
    return p

def square(numOfPoints):
    return [(random.randint(0,100),random.randint(0,100)) for i in range(numOfPoints)]

def onCurve(numOfPoints):
    p = []
    for i in range(numOfPoints):
        val = random.randint(0,100)
        p.append((val**2,val))
    return p
