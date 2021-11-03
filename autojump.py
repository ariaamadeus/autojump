import pyautogui as pyg
import cv2
import numpy as np

mon = {'left': 0, 'top': 0, 'width': 1000, 'height': 1000}
sct = mss()

gameImg = cv2.imread('Tes1.jpeg',cv2.IMREAD_UNCHANGED)
normalImg = cv2.imread('Normalblock.jpeg',cv2.IMREAD_UNCHANGED)
trampolineImg = cv2.imread('Trampolineblock.jpeg',cv2.IMREAD_UNCHANGED)
superImg = cv2.imread('Superblock.jpeg',cv2.IMREAD_UNCHANGED)
while True:
    sct_img = pyg.screenshot()
    sct_img = cv2.cvtColor(np.array(sct_img), cv2.COLOR_RGB2BGR)
    result = cv2.matchTemplate(sct_img,normalImg,cv2.TM_CCOEFF_NORMED)
    minVal,maxVal,minLoc,maxLoc = cv2.minMaxLoc(result)
    normW = normalImg.shape[1]
    normH = normalImg.shape[0]
    threshold = 0.9
    yLoc,xLoc = np.where(result >= threshold)
    rectangles = []
    lowest = 0
    count = 0
    third = 0
    for (x,y) in zip(xLoc,yLoc):
        rectangles.append([int(x),int(y),int(normW),int(normH)])
        rectangles.append([int(x),int(y),int(normW),int(normH)])
    rectangles, weights = cv2.groupRectangles(rectangles,1,0.2)
    for (x,y,w,h) in rectangles:
        if y>lowest and third < 3:
            lowest = count
            third+=1
        count+=1
        cv2.rectangle(sct_img, (x,y),(x+w,y+h),(0,255,255),2)
    if len(rectangles) >= 3:
        x,y,w,h = rectangles[lowest]
        cv2.rectangle(sct_img, (x,y),(x+w,y+h),(255,0,255),2)
    cv2.imshow('screen', np.array(sct_img))
    pyg.moveTo(x,y)
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break


# cv2.imshow('result',result)
cv2.imshow('game',gameImg)
print('show')
cv2.waitkey()
print('close')
cv2.destroyAllwindows()
