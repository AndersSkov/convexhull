import statistics
import time

import pulp
import numpy as np
from matplotlib import pyplot as plt

import Points

CHPoints = []

def findUpper(points):
    #if len(points) < 3:
        #return
    #sort the points
    points.sort(key=lambda x: x[0])
    print(points)
    #find the median and partition
    median = points[round(len(points)/2)][0]
    #solve lp to find bridge
    prob = pulp.LpProblem("bridge_lp", pulp.LpMinimize)
    a = pulp.LpVariable("a")
    b = pulp.LpVariable("b")
    prob += a*median + b
    for p in points:
        prob += p[1] <= a*p[0] + b
    prob.solve()
    linepoints = []
    #find out which points are on the line (might be more than two)
    for p in points:
        if p[1] == round(pulp.value(a)*p[0] + pulp.value(b)):
            linepoints.append(p)
    if len(linepoints) < 2:
        return
    #add the points on the line to the set of CH points
    CHPoints.extend(linepoints)
    #prune points between endpoints and call recursively on left and right points
    left = []
    right = []
    for p in points:
        if not(linepoints[0][0] < p[0]):
            left.append(p)
        elif not(p[0] < linepoints[-1][0]):
            right.append(p)
    findUpper(left)
    findUpper(right)

def findLower(points):
    if len(points) < 3:
        return
    #sort the points
    points.sort(key=lambda x: x[0])
    print(points)
    #find the median and partition
    median = points[round(len(points)/2)][0]
    #solve lp to find bridge
    prob = pulp.LpProblem("bridge_lp", pulp.LpMaximize)
    a = pulp.LpVariable("a")
    b = pulp.LpVariable("b")
    prob += a*median + b
    for p in points:
        prob += p[1] >= a*p[0] + b
    prob.solve()
    linepoints = []
    #find out which points are on the line (might be more than two)
    for p in points:
        if p[1] == round(pulp.value(a)*p[0] + pulp.value(b)):
            linepoints.append(p)
    if len(linepoints) < 2:
        return
    #add the points on the line to the set of CH points
    CHPoints.extend(linepoints)
    #prune points between endpoints and call recursively on left and right points
    left = []
    right = []
    for p in points:
        if not(linepoints[0][0] < p[0]):
            left.append(p)
        elif not(p[0] < linepoints[-1][0]):
            right.append(p)
    findLower(left)
    findLower(right)

testpoints = Points.square(50)
findUpper(testpoints)
findLower(testpoints)

print(CHPoints)
plt.figure()
x = [a[0] for a in testpoints]
y = [b[1] for b in testpoints]
plt.scatter(x, y)

plt.figure()
x1 = [a[0] for a in CHPoints]
y1 = [b[1] for b in CHPoints]
plt.scatter(x1,y1)
plt.show()