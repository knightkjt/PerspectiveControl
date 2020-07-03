import cv2
import numpy as np
import time

#import pdb
#pdb.set_trace()

pSrc = [(  32,0),( 191,  0),( 220, 288),(  8 , 288)]
pDst = [(  0,0),( 224 ,  0),( 224 , 299),(  0 , 299)]
def srcMouse(event, x, y, flags,params):
    global pSrc
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print ('clear src points {} - {}'.format(len(pSrc), pSrc))
        pSrc=[]
        return
    if event == cv2.EVENT_LBUTTONDOWN:
        print ('add point {} - ({}, {})'.format(len(pSrc), x, y))
        if len(pSrc) >=4:
            print ('clear src points {} - {}'.format(len(pSrc), pSrc))
            return
        pSrc.append((x,y))
        #print (np.array(pSrc,dtype=np.float32))

def dstMouse(event, x, y, flags,params):
    global pDst
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print ('clear dst points {} - {}'.format(len(pDst), pDst))
        pDst=[]
        return
    if event == cv2.EVENT_LBUTTONDOWN:
        print ('add point {} - ({}, {})'.format(len(pDst), x, y))
        if len(pDst) >=4:
            print ('clear dst points {} - {}'.format(len(pDst), pDst))
            return
        pDst.append((x,y))

cv2.namedWindow('src')
cv2.setMouseCallback('src', srcMouse)
cv2.namedWindow('dst')
cv2.setMouseCallback('dst', dstMouse)

im = cv2.imread('./notre.jpg')
dst = np.zeros(im.shape,dtype=np.uint8)
print ('clear src points {} - {}'.format(len(pSrc), pSrc))
print ('clear dst points {} - {}'.format(len(pDst), pDst))

while(1):
    imD = im.copy()
    dstD = dst.copy()
    if (len(pSrc) > 0):
        for p in pSrc:
            cv2.circle(imD,p,2,(255,0,0),-1)
    if (len(pDst) > 0):
        for p in pDst:
            cv2.circle(dstD,p,2,(255,0,0),-1)

    if len(pSrc)==4 and len(pDst)==4:
        H = cv2.findHomography(np.array(pSrc,dtype=np.float32),np.array(pDst,dtype=np.float32),cv2.LMEDS)
        dstD=cv2.warpPerspective(imD,H[0],(dstD.shape[1],dstD.shape[0]))
    cv2.imshow('src',imD)
    cv2.imshow('dst',dstD)
    if cv2.waitKey(1) ==27: # ESC
        exit(0)    
    #time.sleep(1)
