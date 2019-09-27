#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 16:22:47 2019

@author: edwin
"""

import cv2
img = cv2.imread('test.jpg',0)
ret,thresh = cv2.threshold(img,127,255,0)
image,contours, hierarchy = cv2.findContours(thresh,1,2)
cnt = contours[0]
M = cv2.moments(cnt)

cnt2 = cnt.reshape(len(cnt))
print(cnt2)