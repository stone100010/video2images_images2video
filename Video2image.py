# -*- coding: utf-8 -*-
"""
Created on Fri May  1 17:59:01 2020

@author: lwang
"""

#%% Video to Image (Frames) conversion
import cv2

file_path = './videos/Nijmegenroad3.mp4'
save_path = './frames/'  # do not miss the last '/'! 
frameRate = 0.2 #//it will capture image in each 0.5 second


vidcap = cv2.VideoCapture(file_path)
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite(save_path+"frame"+str(count)+".jpg", image)     # save frame as JPG file
    else:
        print('cannot find video...')
    return hasFrames

sec = 0
count=1
success = getFrame(sec)
while success:
    print ('Creating...frame ' + str(count))
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)
    
       
#%% Images (Frames) to Video
import cv2
import numpy as np
import os
from os.path import isfile, join

pathIn= './out/' # do not miss the last '/'! 
pathOut = 'nijmegen3_1x.mp4' # or mp4, .avi etc.

fps = 2*1 # how many frames in one sec

frame_array = []
files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
#for sorting the file names properly
files.sort(key = lambda x: int(x[5:-4])) #given name format: frame23.jpg
# files.sort()

for i in range(len(files)):
    filename= pathIn + files[i]
    print ('processing... ' + filename)
    #reading each files
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    
    #inserting the frames into an image array
    frame_array.append(img)
    
out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
for i in range(len(frame_array)):
    # writing to a image array
    out.write(frame_array[i])
    
out.release()

