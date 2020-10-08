from pprint import pprint

from mpl_toolkits.mplot3d import Axes3D
from video2bvh.bvh_skeleton import coco_skeleton
import numpy as np
import matplotlib.pyplot as plt
from bvh_skeleton import muco_3dhp_skeleton
def xnect_to_bvh(raw2d_file, raw3d_file, ik3d_file):
    p2d = np.loadtxt(raw2d_file)
    p3d = np.loadtxt(raw3d_file)
    i3d = np.loadtxt(ik3d_file)
    num_people = int(np.max(p2d.T[1]) + 1)
    size = i3d.shape[0]
    pred = []
    for i in range(p3d.shape[0]):
        # set dictionary
        pred.append({
            "pred2d": np.zeros([num_people, 14, 2]),
            "pred3d": np.zeros([num_people, 21, 3]),
            "ik3d": np.zeros([num_people, 21, 3]),
            "vis": np.zeros([num_people, 14, 1]),
            "valid_raw": np.zeros([10], dtype=bool),
            "valid_ik": np.zeros([10], dtype=bool)
        })
    # iterate through keyframes of p3d
    for i in range(p3d.shape[0]):
        idx = int(p2d[i][0])
        pidx = int(p2d[i][1])
        pred[idx]["pred2d"][pidx] = np.reshape(p2d[i][2:], [14, 2])
        tmp = np.reshape(p3d[i][2:], [21, 3]).T
        tmp[:2] *= -1
        tmp = tmp.T

        pred[idx]["pred3d"][pidx] = tmp - tmp[14]
        pred[idx]["valid_raw"][pidx] = True
        pred[idx]["vis"][pidx] = (np.greater(pred[idx]["pred2d"][pidx].T[0], 0) &
                                  np.greater(pred[idx]["pred2d"][pidx].T[1], 0)).reshape([14, 1])

    for i in range(i3d.shape[0]):
        idx = int(i3d[i][0])
        pidx = int(i3d[i][1])
        print(pidx)
        tmp = np.reshape(i3d[i][2:], [21, 3]).T
        tmp[:2] *= -1
        tmp = tmp.T

        pred[idx]["ik3d"][pidx] = tmp - tmp[14]
        pred[idx]["valid_ik"][pidx] = True
    return pred

print("loaded the array")

pred = xnect_to_bvh("/home/worker/Repos/xnect/xnect-src/bin/Release/output/raw2D.txt",
                    "/home/worker/Repos/xnect/xnect-src/bin/Release/output/raw3D.txt",
                    "/home/worker/Repos/xnect/xnect-src/bin/Release/output/IK3D.txt")

keypoints = []
for cu in pred:
    keypoints.append(cu["ik3d"][2])

print("Saving bvh")
skel = muco_3dhp_skeleton.Muco3DHPSkeleton()
channels, header = skel.poses2bvh(np.array(keypoints), output_file="test1.bvh")
