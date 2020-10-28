# -*- coding: utf-8 -*-
# @Time : 2020/8/21 下午10:27
# @Author : Odyssey Warsaw
# @File : img2video.py


import cv2
import numpy as np
import os
from os.path import isfile, join

pathIn = 'F:/hsc_share/DeepFaceLab_All_Test/DeepFaceLab_NVIDIA1026/workspace/data_dst/merged102814-mkl-m/'  # do not miss the last '/'!
pathOut = 'F:/hsc_share/DeepFaceLab_All_Test/DeepFaceLab_NVIDIA1026/workspace/data_dst/merged102814-mkl-m.mp4'  # .mp4, or .avi etc.

fps = 24  # how many frames in one sec

frame_array = []
files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
print("files", files)
# for sorting the file names properly
files.sort(key=lambda x: int(x[:-4]))  # given name format: frame23.jpg
# files.sort()

for i in range(len(files)):
    filename = pathIn + files[i]
    print('processing... ' + filename)
    # reading each files
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)

    # inserting the frames into an image array
    frame_array.append(img)

out = cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
for i in range(len(frame_array)):
    # writing to a image array
    out.write(frame_array[i])

out.release()
