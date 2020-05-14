# author:nannan
# contact: zhaozhaoran@bupt.edu.cn
# datetime:2020/5/14 9:02 上午
# software: PyCharm

import my_helpers
import student

path1="pump01/DSC_0001.JPG"
path2="pump01/DSC_0003.JPG"

keypoint01,keypoint02=my_helpers.findMatchesUp(path1, path2)
F=student.get_fundamental(keypoint01,keypoint02)
M1,M2=student.get_camera(F)
my_3dpoints=student.workout_3d(keypoint01,keypoint02,M1,M2)
my_3dpoints=[1,2,3,4,5]
my_helpers.save_3d(my_3dpoints)


