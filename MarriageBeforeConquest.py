import pulp
from matplotlib import pyplot as plt
import math

import Points

CHPoints = []


def findUpper(points):
    # sort the points
    points.sort(key=lambda x: x[0])
    # find the median and partition
    median = points[math.floor(len(points) / 2)][0]
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
    if len(linepoints) == 0:
        return
    # add the points on the line to the set of CH points
    CHPoints.extend(linepoints)
    # prune points between endpoints and call recursively on left and right points
    left = []
    right = []
    for p in points:
        if not (linepoints[0][0] < p[0]):
            left.append(p)
        elif not (p[0] < linepoints[-1][0]):
            right.append(p)
    if len(left) < 3:
        #CHPoints.append(left[0])
        return
    else:
        findUpper(left)
    if len(right) < 3:
        #CHPoints.append(right[-1])
        return
    else:
        findUpper(right)

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
        if not (linepoints[0][0] < p[0]):
            left.append(p)
        elif not (p[0] < linepoints[-1][0]):
            right.append(p)
    if len(left) < 3:
        #CHPoints.append(left[0])
        return
    else:
        findLower(left)
    if len(right) < 3:
        CHPoints.append(right[-1])
        return
    else:
        findLower(right)





if __name__ == "__main__":
    testpoints = Points.square(20)
    findUpper(testpoints)
    #findLower(testpoints)

    print(CHPoints)
    plt.figure()
    x = [a[0] for a in testpoints]
    y = [b[1] for b in testpoints]
    plt.scatter(x, y)

    plt.figure()
    x1 = [a[0] for a in CHPoints]
    y1 = [b[1] for b in CHPoints]
    plt.scatter(x1, y1)
    plt.show()
