import pyautogui as pyg
import cv2
import numpy as np
xsave = 0
ysave = 0
samecount = 5
samebuff = samecount
themin = 0
while True:
    sct_img1 = pyg.screenshot()
    sct_img1 = cv2.cvtColor(np.array(sct_img1), cv2.COLOR_RGB2BGR)
    sct_img = cv2.cvtColor(sct_img1, cv2.COLOR_BGR2HSV)
    masknorm = cv2.inRange(sct_img, (35,175,111), (43,255,167))
    masktram = cv2.inRange(sct_img, (86,142,146), (92,255,172))
    masksups = cv2.inRange(sct_img, (18,227,237), (20,255,255))
    masktot = masknorm+masktram+masksups
    cntstot = cv2.findContours(masktot.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    thetot = []
    if len(cntstot) > 0:
        for cnt in cntstot:
            area = cv2.contourArea(cnt)
            ((x, y), radius) = cv2.minEnclosingCircle(cnt)
            if area > 500:
                thetot.append((int(x),int(y),area))
    x,y,areaFetch = thetot[0+themin]
    if xsave > x:
        xmin = xsave-x
    else:
        xmin = x-xsave
    if ysave >= y:
        ymin = ysave-y
    else:
        ymin = y-ysave
    if (ymin<3 or xmin<3) and samebuff > 0:
        print(samebuff)
        samebuff-=1
        x,y,areaFetch = thetot[0+themin]
    elif samebuff == 0:
        samebuff = samecount
        themin=1
        x,y,areaFetch = thetot[0+themin]
    else:
        samebuff = samecount
        themin=0
        x,y,areaFetch = thetot[0]
    xsave = x
    ysave = y
    pyg.moveTo(x,y)
