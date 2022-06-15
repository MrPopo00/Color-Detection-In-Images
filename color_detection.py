import cv2
from cv2 import rectangle
import numpy as np
import pandas as pd

img_path = 'testimage.jpg'

#Reading the image with opencv
img = cv2.imread(img_path)

clicked = False
r = g = b = xpos = ypos = 0

#reading the colors.csv file and also giving the coloumns name
idx=["color","color_name","hex","R","G","B"]
csv = pd.read_csv('diffrent_colors.csv', names=idx, header=None)

#function to calculate the minimum distance from the colors in the csv file and get the most matching color
def getColorName(R,G,B):
    minimum = 8000
    for i in range(len(csv)):
        distance = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(distance<=minimum):
            minimum = distance
            cname = csv.loc[i,"color_name"]
    return cname

#function for getting the x and y coordinate, when mouse double clicked
def draw_function(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)
       
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_function)

while(1):

    cv2.imshow("image",img)
    if (clicked):
        cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)

        #Creating text string to display( Color name and RGB values )
        text = getColorName(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)

        cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)

        #For very light colours we will display text in black colour
        if(r+g+b>=600):
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
            
        clicked=False

    #Break the loop when user hits 'q' key    
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
