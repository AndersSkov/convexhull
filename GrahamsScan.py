import random
import Points
import matplotlib.pyplot as plt
from operator import ge, le
import timeit

def findHull(uppersign, lowersign, points):
    points.sort(key=lambda x:x[0])
    CH = []
    UH = hull(uppersign, points)
    LH = hull(lowersign, points)

    LH.pop(-1); LH.pop(0); LH.reverse()
    CH.extend(UH); CH.extend(LH)
    
    return CH

def hull(sign, points):
    # Remove the sorting from the line below when running graham scan, and keep in when running Chan's
    points.sort(key=lambda x:x[0])
    hp = []
    hp.append(points[0]); hp.append(points[1])

    for i in range(2,len(points)):
        while len(hp) >= 2 and sign(orientation(hp[-2], hp[-1], points[i]), 0):
            hp.pop(-1)
        hp.append(points[i])

    return hp


def orientation(p1,p2,p3):
    return (p1[0] * (p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1]))


if __name__ == "__main__":
    points = Points.onCurve(1000000)
    upper = ge; lower = le
    
    start = timeit.default_timer()
    CHpoints = findHull(upper, lower, points)
    stop = timeit.default_timer()

    print("Time: ", stop-start)
    print("length: ", len(CHpoints))

    #print("CHpoints", CHpoints)

    #plt.figure()
    #plt.xlim([-5, 105])
    #plt.ylim([-5, 105])
    #x = [a[0] for a in points]
    #y = [b[1] for b in points]
    #plt.scatter(x, y)

    #plt.figure()
    #plt.xlim([-5, 105])
    #plt.ylim([-5, 105])
    #x1 = [a[0] for a in CHpoints]
    #y1 = [b[1] for b in CHpoints]
    #plt.scatter(x1, y1)
    #plt.show()
