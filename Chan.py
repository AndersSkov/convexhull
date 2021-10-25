import math

import numpy as np
from matplotlib import pyplot as plt

import GrahamsScan
from operator import gt, lt, ge, le, sub
import Points
from time import sleep
import timeit


def uh_with_size(points, h):
    partitions = [points[x:x+h] for x in range(0, len(points), h)]
    hulls = []
    for i, partition in enumerate(partitions):
        # list with 3 points or less will always have all points in the convex hull
        if len(partition) < 4:
            hulls.append(partition)
        else:
            hulls.append(GrahamsScan.hull(ge, partition))
    uh = []
    p = min(points, key=lambda x: x[0])
    p_max = max(points, key=lambda x: x[0])
    # upwards ray
    ray = list(map(sub, (p[0], p[1]+1), p))
    for c in range(h):
        # append min p or best tagentpoint
        uh.append(p)

        if p == p_max:
            break

        upperTangents = []
        # Find upper tagent from p to Ui using binary search
        for i in range(len(hulls)):
            # start at half
            current = math.floor(len(hulls[i]) / 2)
            skip = False
            while True:
                # skip if empty
                if len(hulls[i]) == 0 or (len(hulls[i]) == 1 and p == hulls[i][0]):
                    skip = True
                    break
                # check if we are at the last element, so we don't get index out of bounds
                if not current == len(hulls[i])-1:
                    # calculate cross product to see if the point after the current is above or belove tagent
                    v1 = (hulls[i][current][0] - p[0], hulls[i][current][1] - p[1]) 
                    v2 = (hulls[i][current][0] - hulls[i][current+1][0], hulls[i][current][1]-hulls[i][current+1][1])
                    cross = v1[0]*v2[1] - v1[1]*v2[0]

                else:
                    # we were at the last element in hulls[i] so we only need to check if the point before was below.
                    # we do that in case cross > 0, so we set cross to 1
                    cross = 1

                # point after is below, or last element
                if cross > 0:
                    if not current == 0:
                        # check if point before also is below, if it is we have found the upper tangenr
                        v1_2 = (hulls[i][current][0] - p[0], hulls[i][current][1] - p[1]) 
                        v2_2 = (hulls[i][current][0] - hulls[i][current-1][0], hulls[i][current][1]-hulls[i][current-1][1])
                        cross2 = v1_2[0]*v2_2[1] - v1_2[1]*v2_2[0]
                        if cross2 > 0:
                            #print("SUCCESSS")
                            break
                    # point after was below and current is the first point
                    elif current == 0:
                        break 

                    # point before was not below, since cross2 >= 0 we therefore move back in the list
                    remain = len(hulls[i][:current])
                    if remain == 1:
                        current -= 1
                    else:
                        current -= math.floor(remain/2)

                # point after is above, therefore we move up in the list
                if cross < 0:
                    remain = len(hulls[i][current:])-1
                    if remain == 1:
                        current += 1
                    else:
                        current += math.floor(remain/2)


                if cross == 0:
                    # if cross == 0 the point lies on the tagent. If the point is p we increment current by one since we know that 
                    # inside this hull the upper tagent from p is the point after.
                    if p == hulls[i][current]:
                        current += 1
                        #print("SAME POINT")
                        break
                    else:
                        break
            if not skip:
                # add the uppertagent    
                upperTangents.append(hulls[i][current])

        if not len(upperTangents)==0:
            # Find the best upperTagent
            best, bestRay = findBestTangent(ray, p, upperTangents)
            p = best
            ray = bestRay 
            if c+1 == h:
                uh.append(p)
        

        # remove all points from every Ui with x coordinate less than p's
        for j in range(len(hulls)):
            for k, m in enumerate(hulls[j]):
                if m[0] < p[0]:
                    hulls[j].pop(k)
    

    return uh, p == p_max


def upper_hull(points):
    for i in range(math.ceil(math.log2(math.log2(len(points))))):
        exponent = 2 ** (2 ** (i+1))
        hullp, success = uh_with_size(points, exponent)
        if success:
            return hullp


def findBestTangent(ray, p, upperTan): 
    #init angle to be large
    angle = 361


    unitVector1 = (ray / np.linalg.norm(ray)).round(3)
    # calculate vector from p to uppertan and angle between that vector and vectorRay
    for point in upperTan:
        # vector from p to point
        vector = list(map(sub, point, p)) 
        unitVector2 = (vector / np.linalg.norm(vector)).round(3)
        dotProduct = np.dot(unitVector1, unitVector2).round(3)
        print("PRIK", dotProduct)
        try:
            a = np.arccos(dotProduct).round(3)
        except:
            if dotProduct > 0:
                 a = np.arccos(1).round(3)
            else:
                a = np.arccos(-1).round(3)


        if a < angle:
            bestPoint = point
            bestRay = vector
            angle = a
    return bestPoint, bestRay


def orientation(p1,p2,p3):
    return (p1[0] * (p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1]))


if __name__ == "__main__":
    testpoints = Points.square(100)

    start = timeit.default_timer()
    hull = upper_hull(testpoints)
    stop = timeit.default_timer()

    print("Time: ", stop-start)
    print("length: ", len(hull))



    #plt.figure()
    #plt.xlim([-5, 105])
    #plt.ylim([-5, 105])
    #x = [a[0] for a in testpoints]
    #y = [b[1] for b in testpoints]
    #plt.scatter(x, y)

    #plt.figure()
    #plt.xlim([-5, 105])
    #plt.ylim([-5, 105])
    ##x1 = [a[0] for a in hull] 
    #y1 = [b[1] for b in hull] 
    #plt.scatter(x1, y1)
    #plt.show()