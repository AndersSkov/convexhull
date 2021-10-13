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
    for i in range(h):
        uh.append(p)
        if points[i] == p_max:
            break
        t = 0
        for j in range(len(partitions[i])-1):
            slope = (partitions[i][j][1]-p[1])/(partitions[i][j][0]-p[0])
            if slope > t:
                t = slope
                tangentpoint = partitions[i][j]
        p = tangentpoint
        l = t




if __name__ == "__main__":
