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
        x = round(center[0] + r * math.cos(theta))
        y = round(center[1] + r * math.sin(theta))
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

def triangle(numOfPoints):
    p = []
    half = numOfPoints/2
    corner1 = (0,0); corner2 = (numOfPoints,0); corner3 = (half,numOfPoints)
    for i in range(numOfPoints):
        r1 = random.random()
        r2 = random.random()

        s1 = math.sqrt(r1)

        x = round(corner1[0] * (1.0 - s1) + corner2[0] * (1.0 - r2) * s1 + corner3[0] * r2 * s1)
        y = round(corner1[1] * (1.0 - s1) + corner2[1] * (1.0 - r2) * s1 + corner3[1] * r2 * s1)

        p.append((x,y))
    return p