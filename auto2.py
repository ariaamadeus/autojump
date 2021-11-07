import pyautogui as p
import cv2 as c
import numpy as n
import win32api as w
a = 451
b = 105
while True:
    d = p.screenshot(region = (a,b,910,726))
    d = c.resize(n.array(d),(256,144))
    d = c.cvtColor(d, c.COLOR_RGB2HSV)
    e = c.inRange(d, (35,175,111), (43,255,167))
    f = c.inRange(d, (86,142,146), (92,255,172))
    g = c.inRange(d, (18,227,237), (20,255,255))
    h = e+f+g
    j = c.inRange(d, (14,115,226), (16,126,255))
    k = c.findContours(h.copy(), c.RETR_EXTERNAL, c.CHAIN_APPROX_SIMPLE)[-2]
    l = c.findContours(j.copy(), c.RETR_EXTERNAL, c.CHAIN_APPROX_SIMPLE)[-2]
    m = []
    r = []
    if len(k) > 0:
        for i in k:
            if c.contourArea(i) > 30:
                m.append(c.minEnclosingCircle(i)[0])
    if len(l) > 0:
        for i in l:
            if c.contourArea(i) > 20:
                r.append(c.minEnclosingCircle(i)[0])
    if len(m)>0:
        if len(m)>=2:
            x,y = m[1]
        else:
            x,y = m[0]
        o,q = r[0]
        if q+18 < y:
            if len(m)>=2:
                x,y = m[1]
            else:
                x,y = m[0]
        else:
            x,y = m[0]
        w.SetCursorPos((int(x*3.6+a),int(y*5+b)))
    else:
        print('NOL')
