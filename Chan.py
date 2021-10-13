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
    
    t = 0
    for i in range(h):
        uh.append(p)
        if points[i] == p_max:
            break
        best = float('inf')
        # first iteration in loop h, where we only calculate slope to see least angle
        for j in range(len(partitions[i])-1):
            if i == 0:
                slope = (partitions[0][j][1]-p[1])/(partitions[0][j][0]-p[0])
                if slope > t:
                    t = slope
                    tangentpoint = partitions[i][j]
            else:
                ori = orientation(uh[-2], uh[-1], partitions[i][j])
                if ori >= 0 and ori < best:
                    tangentpoint = partitions[i][j]
        p = tangentpoint


def orientation(p1,p2,p3):
    return (p1[0] * (p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1]))


if __name__ == "__main__":
