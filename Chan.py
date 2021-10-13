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
    
    least = float('-inf')
    for i in range(h):
        # if hulls is empty, continue to next iteration 
        if len(hulls[i]) == 0:
            continue

        uh.append(p)
        if points[i] == p_max:
            break
        best = float('inf')
        #init tagentpoint to be whatever
        tangentpoint = hulls[0][0]
        # first iteration in loop h, where we only calculate slope to see least angle
        for j in range(len(hulls[i])-1):
            if i == 0:
                slope = (hulls[0][j][1]-p[1])/(hulls[0][j][0]-p[0])
                if slope > least:
                    least = slope
                    tangentpoint = hulls[i][j]
            else:
                ori = orientation(uh[-2], uh[-1], hulls[i][j])
                if ori >= 0 and ori < best:
                    tangentpoint = hulls[i][j]
        p = tangentpoint
        for j in range(len(hulls)-1):
            for k in hulls[j]:
                if k[0] < p[0]:
                    hulls[j].remove(k)


def orientation(p1,p2,p3):
    return (p1[0] * (p2[1]-p3[1]) + p2[0]*(p3[1]-p1[1]) + p3[0]*(p1[1]-p2[1]))


if __name__ == "__main__":
