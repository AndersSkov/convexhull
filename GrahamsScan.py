import random
import Points
import matplotlib.pyplot as plt
from operator import gt, lt, ge, le

points = Points.circle(200)

def hall(sign):
    hallpoints = []
    hallpoints.append(points[0])
    hallpoints.append(points[1])
    for i in range(2,len(points)):
        while len(hallpoints) >= 2 and sign(orientation(hallpoints[-2], hallpoints[-1], points[i]), 0):
            print("popping:", hallpoints[-1])
            hallpoints.pop(-1)
        hallpoints.append(points[i])
    return hallpoints

def orientation(p1,p2,p3):
    return (p1[0] * (p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1]))


def hall2(h):
    CHpoints.append(points[0])
    CHpoints.append(points[1])
    for i in range(2,len(points)):
        while len(CHpoints) >= 2 and orientation2(CHpoints[-2], CHpoints[-1], points[i]) in h:
            print("popping:", CHpoints[-1])
            CHpoints.pop(-1)
        CHpoints.append(points[i])


def orientation2(p1, p2, p3):
    val = (float(p2[1] - p1[1]) * (p3[0] - p2[0])) - (float(p2[0] - p1[0]) * (p3[1] - p2[1]))
    if (val > 0):
        # right turn
        return 1
    elif (val < 0):
        # left turn
        return 2
    else:
        # straight
        return 0
    

CHpoints = []
points.sort(key=lambda x:x[0])
upper = le; lower = ge
upperHall = hall(upper)
lowerHall = hall(lower)
lowerHall.pop(-1); lowerHall.pop(0); lowerHall.reverse()
CHpoints.extend(upperHall); CHpoints.extend(lowerHall)

#hall2(h=[2,0])
#hall2(h=[1,0])

print("points", points)
print("CHpoints", CHpoints)


x = [a[0] for a in points]
y = [b[1] for b in points]
plt.scatter(x, y)
x1 = [a[0] for a in CHpoints]
y1 = [b[1] for b in CHpoints]
plt.plot(x1,y1)
plt.show()
