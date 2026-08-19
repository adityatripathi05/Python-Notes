#!/usr/bin/env python
# coding: utf-8

# In[2]:


# !pip install opencv-python


# In[1]:


#import ml libraries
import numpy as np
import pandas as pd
import cv2


# In[14]:


#storing image path
img_path='./Dataset/colorpic.jpg'
#Reading the image with opencv
img = cv2.imread(img_path)


# In[15]:


# print(type(img))


# In[16]:


print(img.shape)


# In[ ]:


cv2.imshow('window1', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[17]:


#Reading csv file with pandas and giving names to each column
index=["color","color_name","hex","R","G","B"]
csv = pd.read_csv('./Dataset/colors.csv', names=index, header=None)
csv.head()


# In[18]:


#function to calculate minimum distance from all colors and get the most matching color
# d = abs(Red – ithRedColor) + (Green – ithGreenColor) + (Blue – ithBlueColor)
def getColorName(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = csv.loc[i,"color_name"]
    return cname


# In[19]:


#function to get x,y coordinates of mouse double click
def draw_function(event, x,y,flags,param): # event and coordinates of the mouse position
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)


# In[21]:


#declaring global variables
clicked = False
r = g = b = xpos = ypos = 0

# created a window in which the input image will display       
cv2.namedWindow('image')

#set a callback function which will be called when a mouse event happens
cv2.setMouseCallback('image',draw_function)
# Callback will call the draw_function() whenever a mouse event occurs with the proper event and coordinates

while(1):
    cv2.imshow("image",img)
    if (clicked):
        #cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle 
        cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)

        #Creating text string to display( Color name and RGB values )
        text = getColorName(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
        
        #cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)

        #For very light colours we will display text in black colour
        if(r+g+b>=600):
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
            
        clicked=False

    #Break the loop when user hits 'esc' key    
    if cv2.waitKey(20) & 0xFF ==27:
        break
    
cv2.destroyAllWindows()


# In[ ]:




