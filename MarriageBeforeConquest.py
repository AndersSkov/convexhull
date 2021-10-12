import pulp
from matplotlib import pyplot as plt
import math
import random

import Points

CHPoints = []


def findUpper(points):
    # find the median and partition
<<<<<<< HEAD
    median = points[math.floor(len(points) / 2)][0] 
=======
    median = points[random.randint(0, len(points)-1)][0]
>>>>>>> 757e8329630289fb9883c1f2372ad9bce8f909d3
    # solve lp to find bridge
    prob = pulp.LpProblem("bridge_lp", pulp.LpMinimize)
    a = pulp.LpVariable("a")
    b = pulp.LpVariable("b")
    prob += a * median + b
    for p in points:
        prob += p[1] <= a * p[0] + b
    prob.solve()
    linepoints = []
    # find out which points are on the line
    for p in points:
        if p[1] == round(pulp.value(a) * p[0] + pulp.value(b)):
            linepoints.append(p)
    if len(linepoints) < 2:
        return
    # add the points on the line to the set of CH points
    CHPoints.extend(linepoints)
    # prune points between endpoints and call recursively on left and right points
    left = []
    right = []
    for p in points:
        if p[0] <= linepoints[0][0]:
            left.append(p)
        elif linepoints[-1][0] <= p[0]:
            right.append(p)
    if len(right) < 3:
        return
    else:
        findUpper(right)
    if len(left) < 3:
        return
    else:
        findUpper(left)

def findLower(points):
    # sort the points
    points.sort(key=lambda x: x[0])
    # find the median and partition
    median = points[math.floor(len(points) / 2)][0]
    # solve lp to find bridge
    prob = pulp.LpProblem("bridge_lp", pulp.LpMaximize)
    a = pulp.LpVariable("a")
    b = pulp.LpVariable("b")
    prob += a * median + b
    for p in points:
        prob += p[1] >= a * p[0] + b
    prob.solve()
    linepoints = []
    # find out which points are on the line (might be more than two)
    #if pulp.value(a) is not None:
    for p in points:
        if p[1] == round(pulp.value(a) * p[0] + pulp.value(b)):
            linepoints.append(p)
    if len(linepoints) == 0:
        return
    # add the points on the line to the set of CH points
    CHPoints.extend(linepoints)
    # prune points between endpoints and call recursively on left and right points
    left = []
    right = []
    for p in points:
        if p[0] <= linepoints[0][0]:
            left.append(p)
        elif linepoints[-1][0] <= p[0]:
            right.append(p)
    if len(left) < 2:
        #CHPoints.append(left[0])
        return
    else:
        findLower(left)
    if len(right) < 2:
        CHPoints.append(right[-1])
        return
    else:
        findLower(right)


def prune(points):
    pl = points[0]
    pr = points[-1]
    for p in points:
        if p[0] < pl[0]:
            pl = p
        elif  p[0] == pl[0] and p[1] > pl[1]:
            pl = p   

        if p[0] > pl[0]:
            pr = p
        elif p[0] == pl[0] and p[1] < pl[1]:
            pr = p

    slope = (pl[1]-pr[1]) / (pl[0]- pr[0])
    c = (pr[1] - (slope * pr[0]))
    
    for i, p in enumerate(points):
        if p[1] < slope * p[0]+c:
            points.pop(i)

    return points


if __name__ == "__main__":
    testpoints = Points.square(20)
    findUpper(testpoints)
    #findLower(testpoints)

    print(CHPoints)
    plt.figure()
    plt.xlim([-5, 105])
    plt.ylim([-5, 105])
    x = [a[0] for a in testpoints]
    y = [b[1] for b in testpoints]
    plt.scatter(x, y)

    plt.figure()
    plt.xlim([-5,105])
    plt.ylim([-5, 105])
    x1 = [a[0] for a in CHPoints]
    y1 = [b[1] for b in CHPoints]
    plt.scatter(x1, y1)
    plt.show()
