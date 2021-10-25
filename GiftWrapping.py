import random
import matplotlib.pyplot as plt
import math
import Points
import timeit


def findHull(points):
    hullPoints = []
    start = min(points, key=lambda x: x[0])
    startIndex = points.index(start)
    hullPoints.append(start)
    curIndex = startIndex

    while True:
        # index of next point
        q = (curIndex + 1) % len(points)

        for i in range(len(points)):
            if i == curIndex:
                continue
            
            # check if there is another left turn from the current index
            ori = orientation(points[curIndex], points[i], points[q])
            if ori > 0 or (ori == 0 and dist(points[i], points[curIndex]) > dist(points[q], points[curIndex])):
                q = i 

        curIndex = q

        if curIndex == startIndex:
            # done
            break

        hullPoints.append(points[q])
    return hullPoints


def dist(p1, p2):
    return math.sqrt(((p1[0]-p2[0])**2) + ((p1[1]-p2[1])**2))


def orientation(p1,p2,p3):
    return (p1[0] * (p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1]))




if __name__ == "__main__":
    
    points = Points.square(1000000)   
    
    start = timeit.default_timer()
    hullPoints = findHull(points)   
    stop = timeit.default_timer()
    print("Time: ", stop-start)
    print("length: ", len(hullPoints))








#x = [a[0] for a in points]
#y = [b[1] for b in points]
#plt.scatter(x, y)
#x1 = [a[0] for a in hullPoints]
#y1 = [b[1] for b in hullPoints]
#plt.plot(x1,y1)
#plt.show()