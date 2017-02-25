#!/usr/bin/env python
import cv2
import numpy as np
import argparse
import os

#img= cv2.imread('A.png')
#print img.shape
#img2 =img[59:538,393:1032]
path = '/home/djtobias/Downloads/A-Y/Y/'
#cv2.imwrite('messigray.png',img2)
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
        
        

