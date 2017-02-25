#!/usr/bin/env python
import cv2
import numpy as np
import argparse
import os
import random


img= cv2.imread('/home/djtobias/Downloads/DataSet_A-Y/A/A-RGB/A_RGB_0.png')


def augmentImg(img,x,y,):
    height,width,channel = img.shape
    print height,width,channel
    shiftY = int(80*y)
    shiftX = int(240*x)
    ROIx = 400
    ROIy = 400
    img2 = img[(0+shiftY):(ROIy+shiftY),(0+shiftX):(ROIx+shiftX)]
    print img2.shape
    return img2
for i in
img3 = augmentImg(img,0.1,0.5)

cv2.imwrite('/home/djtobias/Downloads/A.png',img3)
'''
for i in os.walk(path):
    (root,dirs,files) = i
    num = 0
    for name in files:
        img = cv2.imread(root+'/'+name)
        img2 =img[539:1019,393:1033]
        #cv2.imshow('image',img2)
        #imgPath = os.path.join(root, name))
            
        cv2.imwrite(root+'Y_D_'+str(num)+'.png',img2)
        num = num +1   
'''        
        

