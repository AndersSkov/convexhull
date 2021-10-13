import numpy as np
import GrahamsScan
from operator import gt, lt, ge, le

def uh_with_size(points, h):
    partitions = np.array_split(points, h)
    hulls = []
    for i, partition in enumerate(partitions):
        hulls[i] = GrahamsScan.hall(le, partition)
    uh = []
    p = min(points, key=lambda x: x[0])
    p_max = max(points, key=lambda x: x[0])
    # first iteration in loop h, where we only calculate slope to see least angle
    t = 0
    for j in range(len(partition[0])-1):
        slope = (partitions[0][j][1]-p[1])/(partitions[0][j][0]-p[0])
        if slope > t:
            t = slope
            tangentpoint = partitions[i][j]
    uh.append(p)
    p = tangentpoint


    for i in range(1,h):
        uh.append(p)
        if points[i] == p_max:
            break
        best = float('inf')
        for j in range(len(partitions[i])-1):
            ori = orientation(uh[-2], uh[-1], partitions[i][j])
            if ori >= 0 and ori < best:
                tangentpoint = partitions[i][j]
        p = tangentpoint


def orientation(p1,p2,p3):
    return (p1[0] * (p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1]))


if __name__ == "__main__":
