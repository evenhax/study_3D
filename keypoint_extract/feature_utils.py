import numpy as np
import cv2
import json

def findMatchesUp(path01,path02):

    img1 = cv2.imread(path01, 0)
    img2 = cv2.imread(path02, 0)
    detector = cv2.ORB_create()
    # flann_params = dict(algorithm=6,
    #                     table_number=12,  # 12
    #                     key_size=20,  # 20
    #                     multi_probe_level=2)  # 2
    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=False)

    kp1, desc1 = detector.detectAndCompute(img1, None)
    kp2, desc2 = detector.detectAndCompute(img2, None)

    raw_matches = matcher.knnMatch(desc1, desc2, 2)  # 2

    good = []

    for m, n in raw_matches:
        if m.distance < 0.75 * n.distance:
            good.append(m)

    if len(good) > 10:
        src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
        matchesMask = mask.ravel().tolist()
        print(good)
        print(mask)
        print(matchesMask)
    else:
        print("No enough matches  - %d/%d" % (len(good), 10))
        matchesMask = None

    draw_params = dict(matchColor=(0, 255, 0),  # draw matches in green color
                       singlePointColor=(0, 0, 255),
                       matchesMask=matchesMask,
                       flags=2)  # draw only inliers

    vis = cv2.drawMatches(img1, kp1, img2, kp2, good, None, **draw_params)
    # cv2.imshow("", vis)
    cv2.imwrite("thismatch.jpg", vis)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    storeMatches(kp1,kp2,good,matchesMask)
    return matchesMask, good

def storeMatches(kp1,kp2,matchList, myMask):
    dict={}
    n=len(myMask)
    k=0
    for i in range(n):
        if(myMask[i]):
            x1=kp1[matchList[i].queryIdx].pt
            x2=kp2[matchList[i].trainIdx].pt
            key="pair"+str(k)
            val={'img01':x1,'img02':x2}
            dict[key]=val
            k=k+1
    print (dict)
    js = json.dumps(dict)
    file = open('match_pair.txt', 'w')
    file.write(js)
    file.close()


if __name__ == '__main__':
    path1="pump01/DSC_0001.JPG"
    path2="pump01/DSC_0003.JPG"
    findMatchesUp(path1,path2)
