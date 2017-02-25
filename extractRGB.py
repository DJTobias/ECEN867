#!/usr/bin/env python
import cv2
import numpy as np
import argparse
import os

path = '/home/djtobias/Downloads/A-Y/Y/'

for i in os.walk(path):
    (root,dirs,files) = i
    num = 0
    for name in files:
        img = cv2.imread(root+'/'+name)
        img2 =img[59:539,393:1033]   
        cv2.imwrite(root+'Y_RGB_'+str(num)+'.png',img2)
        num = num +1   
        
        

