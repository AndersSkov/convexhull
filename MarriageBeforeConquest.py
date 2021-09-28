import statistics
import pulp
import numpy as np
from matplotlib import pyplot as plt

import Points

CHPoints = []

def findHull(points):
    #sort the points
    points.sort(key=lambda x: x[0])
    #find the median and partition
    median = points[round(len(points)/2)][0]
    left = []
    right = []
    for p in points:
        if p[0] < median:
            left.append((p[0], p[1]))
        else:
            right.append((p[0], p[1]))
    #solve lp to find bridge
    prob = pulp.LpProblem("bridge_lp", pulp.LpMinimize)
    a = pulp.LpVariable("a")
    b = pulp.LpVariable("b")
    prob += a*median + b
    for p in points:
        prob += p[1] <= a*p[0] + b
    prob.solve()
    endpoints = []
    #find out which points are on the line (might be more than two)
    for p in points:
        if p[1] == round(pulp.value(a)*p[0] + pulp.value(b)):
            endpoints.append(p)
    print(endpoints)
    CHPoints.append(endpoints[0])
    CHPoints.append(endpoints[len(endpoints)-1])
    endpoints.sort(key=lambda x: x[0])
    #remove points between the endpoints
    for p in points:
        if endpoints[0][0] < p[0] < endpoints[len(endpoints) - 1][0]:
            points.remove(p)
    left = []
    right = []
    for p in points:
        if p[0] < endpoints[0][0]:
            left.append(p)
        elif p[0] > endpoints[len(endpoints)-1][0]:
            right.append(p)
    #findHull(left)
    #findHull(right)
    x = [a[0] for a in points]
    y = [b[1] for b in points]
    plt.scatter(x, y)

testpoints = Points.square()
findHull(testpoints)

print(CHPoints)

#x = [a[0] for a in testpoints]
#y = [b[1] for b in testpoints]
#plt.scatter(x, y)
x1 = [a[0] for a in CHPoints]
y1 = [b[1] for b in CHPoints]
plt.scatter(x1,y1)
plt.show()