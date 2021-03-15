# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 14:40:57 2021

@author: Athrva Pandhare
"""
""" All Imports """
import numpy as np
import cv2
from imutils.video import VideoStream
import pandas as pd

    
def main():
    feed2 = r'C:\Users\Athrva Pandhare\Desktop\Laned.mp4'
    pts = []
    showlive = False
    data = pd.read_csv(r'C:\Users\Athrva Pandhare\Desktop\DIPLIB MasterCode\roi_lane.csv')
    
    cap = cv2.VideoCapture(feed2)
    ret, frame = cap.read()
    for i in range(len(data['x'].values)):
        
        pts.append((data['x'].iloc[i], data['y'].iloc[i] ))
        #print(pts)
    mask1 = np.zeros(frame.shape, np.uint8)
    points = np.array(pts, np.int32)
    points = points.reshape((-1, 1, 2))

    #print(points)
    if len(points) > 0 :
        showlive = True 
        videocapture =  VideoStream(src=feed2).start()

    mask2 = cv2.fillPoly(mask1.copy(), [points], (255, 255, 255))
    minLineLength = 35
    maxLineGap = 0
    
    while showlive and len(pts) > 0:
        
        frame = videocapture.read()
        key = cv2.waitKey(1)
        if frame is None:
            videocapture.stop()
            break
    
        try:
            ROI = cv2.bitwise_and(mask2, frame)
        except:
            videocapture.stop()
            break
        img = cv2.cvtColor(np.copy(ROI), cv2.COLOR_BGR2GRAY) # convert to single channel
        mask_ = np.zeros(frame.shape)
        
        ret,edges = cv2.threshold(img,195,255,cv2.THRESH_BINARY)
        kernel = np.ones((5,5),np.uint8)
        edges = cv2.dilate(edges,kernel,iterations = 3)
        contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE,
                                               cv2.CHAIN_APPROX_NONE)
        contours = sorted(contours, key = cv2.contourArea, reverse = True)
        

        cv2.drawContours(frame, contours, -1, (0,0,245), 5)

        cv2.imshow("raw", frame)
    
        if key & 0xFF == ord('q'):
            break
    return
    
if __name__ == '__main__':
    main()
    