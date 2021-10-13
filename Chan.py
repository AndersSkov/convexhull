import math

import numpy as np
from matplotlib import pyplot as plt

import GrahamsScan
from operator import gt, lt, ge, le

import Points


def uh_with_size(points, h):
    partitions = [points[x:x+h] for x in range(0, len(points), h)]
    hulls = []
    for i, partition in enumerate(partitions):
        # list with 3 points or less will always have all points in the convex hull
        if len(partition) < 4:
            hulls.append(partition)
        else:
            hulls.append(GrahamsScan.hall(le, partition))
    uh = []
    p = min(points, key=lambda x: x[0])
    p_max = max(points, key=lambda x: x[0])

    for i in range(h):
        
  

        # remove all points from every Ui with x coordinate less than p's
        for j in range(len(hulls)):
            for k, m in enumerate(hulls[j]):
                if m[0] < p[0]:
                    hulls[j].pop(k)
    
    return uh, p == p_max

def upper_hull(points):
    for i in range(math.ceil(math.log2(math.log2(len(points))))):
        exponent = 2 ** (2 ** (i+1))
        print("exponent", exponent)
        hull, success = uh_with_size(points, exponent)
        if success:
            return hull



def orientation(p1,p2,p3):
    return (p1[0] * (p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1]))


if __name__ == "__main__":
    testpoints = Points.square(20)

    hull = upper_hull(testpoints)

    plt.figure()
    plt.xlim([-5, 105])
    plt.ylim([-5, 105])
    x = [a[0] for a in testpoints]
    y = [b[1] for b in testpoints]
    plt.scatter(x, y)

    plt.figure()
    plt.xlim([-5, 105])
    plt.ylim([-5, 105])
    x1 = [a[0] for a in hull]
    y1 = [b[1] for b in hull]
    plt.scatter(x1, y1)
    plt.show()