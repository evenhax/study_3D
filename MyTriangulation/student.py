# author:nannan
# contact: zhaozhaoran@bupt.edu.cn
# datetime:2020/5/14 9:02 上午
# software: PyCharm
import numpy as np
import cv2


def get_fundamental(src_pts, dst_pts):
    F=np.empty([3,3],dtype=float)
    return F

def get_camera(Fundamental):
    M1=np.empty([3,4], dtype = float)
    M2=np.empty([3,4], dtype = float)

    return M1,M2

def workout_3d(src_pts, dst_pts,M1,M2):
    list_3d=[]
    list_out=np.array(list_3d)
    return list_out

