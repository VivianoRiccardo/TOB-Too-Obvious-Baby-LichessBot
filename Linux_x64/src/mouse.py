# import the necessary packages
import numpy as np
import pyautogui
import imutils
import cv2
import argparse
import random
import time

def screenshot():
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imwrite("../img/chessboard.png", image)

# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
refPt = []
cropping = False
image = None

def click_and_crop(event, x, y, flags, param):
    global image
    # grab references to the global variables
    global refPt, cropping
 
    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being
    # performed
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True
 
    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        refPt.append((x, y))
        cropping = False
 
        # draw a rectangle around the region of interest
        cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
        cv2.imshow("image", image)


def get_area():
    # load the image, clone it, and setup the mouse callback function
    global image
    image = cv2.imread("../img/chessboard.png")
    clone = image.copy()
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", click_and_crop)
     
    # keep looping until the 'q' key is pressed
    while True:
        # display the image and wait for a keypress
        cv2.imshow("image", image)
        key = cv2.waitKey(1) & 0xFF
     
        # if the 'r' key is pressed, reset the cropping region
        if key == ord("r"):
            image = clone.copy()
     
        # if the 'c' key is pressed, break from the loop
        elif key == ord("c"):
            break
     
    # if there are two reference points, then crop the region of interest
    # from teh image and display it
    # close all open windows
    cv2.destroyAllWindows()
    
    return refPt

def click_somewhere(xy,moves,color,waiting):
    #print(xy[0])
    #print(type(xy[0][0]))
    x1 = xy[0][0]
    x2 = xy[1][0]
    y1 = xy[0][1]
    y2 = xy[1][1]
    
    xmax = -1
    xmin = -1
    ymax = -1
    ymin = -1
    
    #print("we")
    #print(moves)
    if(x1 > x2):
        xmax = x1
        xmin = x2
    else:
        xmax = x2
        xmin = x1
    if(y1 > y2):
        ymax = y1
        ymin = y2
    else:
        ymax = y2
        ymin = y1
    
    clickx1 = -1
    clicky1 = -1
    clickx2 = -1
    clicky2 = -1
    
    dimensionxbox = ((xmax-xmin)/8)
    centerxbox = ((xmax-xmin)/16)
    dimensionybox = ((ymax-ymin)/8)
    centerybox = ((ymax-ymin)/16)
    
    if(color == 'white'):
        if(moves[0] == 'a'):
            clickx1 = xmin + centerxbox
        elif(moves[0] == 'b'):
            clickx1 = xmin + dimensionxbox + centerxbox
        elif(moves[0] == 'c'):
            clickx1 = xmin + 2*dimensionxbox + centerxbox
        elif(moves[0] == 'd'):
            clickx1 = xmin + 3*dimensionxbox + centerxbox
        elif(moves[0] == 'e'):
            clickx1 = xmin + 4*dimensionxbox + centerxbox
        elif(moves[0] == 'f'):
            clickx1 = xmin + 5*dimensionxbox + centerxbox
        elif(moves[0] == 'g'):
            clickx1 = xmin + 6*dimensionxbox + centerxbox
        elif(moves[0] == 'h'):
            clickx1 = xmin + 7*dimensionxbox + centerxbox
        
        if(moves[1] == '1'):
            clicky1 = ymax - centerybox
        elif(moves[1] == '2'):
            clicky1 = ymax - dimensionybox - centerybox
        elif(moves[1] == '3'):
            clicky1 = ymax - 2*dimensionybox - centerybox
        elif(moves[1] == '4'):
            clicky1 = ymax - 3*dimensionybox - centerybox
        elif(moves[1] == '5'):
            clicky1 = ymax - 4*dimensionybox - centerybox
        elif(moves[1] == '6'):
            clicky1 = ymax - 5*dimensionybox - centerybox
        elif(moves[1] == '7'):
            clicky1 = ymax - 6*dimensionybox - centerybox
        elif(moves[1] == '8'):
            clicky1 = ymax - 7*dimensionybox - centerybox
        
        if(moves[2] == 'a'):
            clickx2 = xmin + centerxbox
        elif(moves[2] == 'b'):
            clickx2 = xmin + dimensionxbox + centerxbox
        elif(moves[2] == 'c'):
            clickx2 = xmin + 2*dimensionxbox + centerxbox
        elif(moves[2] == 'd'):
            clickx2 = xmin + 3*dimensionxbox + centerxbox
        elif(moves[2] == 'e'):
            clickx2 = xmin + 4*dimensionxbox + centerxbox
        elif(moves[2] == 'f'):
            clickx2 = xmin + 5*dimensionxbox + centerxbox
        elif(moves[2] == 'g'):
            clickx2 = xmin + 6*dimensionxbox + centerxbox
        elif(moves[2] == 'h'):
            clickx2 = xmin + 7*dimensionxbox + centerxbox
        
        if(moves[3] == '1'):
            clicky2 = ymax - centerybox
        elif(moves[3] == '2'):
            clicky2 = ymax - dimensionybox - centerybox
        elif(moves[3] == '3'):
            clicky2 = ymax - 2*dimensionybox - centerybox
        elif(moves[3] == '4'):
            clicky2 = ymax - 3*dimensionybox - centerybox
        elif(moves[3] == '5'):
            clicky2 = ymax - 4*dimensionybox - centerybox
        elif(moves[3] == '6'):
            clicky2 = ymax - 5*dimensionybox - centerybox
        elif(moves[3] == '7'):
            clicky2 = ymax - 6*dimensionybox - centerybox
        elif(moves[3] == '8'):
            clicky2 = ymax - 7*dimensionybox - centerybox
    
    else:
        if(moves[0] == 'h'):
            clickx1 = xmin + centerxbox
        elif(moves[0] == 'g'):
            clickx1 = xmin + dimensionxbox + centerxbox
        elif(moves[0] == 'f'):
            clickx1 = xmin + 2*dimensionxbox + centerxbox
        elif(moves[0] == 'e'):
            clickx1 = xmin + 3*dimensionxbox + centerxbox
        elif(moves[0] == 'd'):
            clickx1 = xmin + 4*dimensionxbox + centerxbox
        elif(moves[0] == 'c'):
            clickx1 = xmin + 5*dimensionxbox + centerxbox
        elif(moves[0] == 'b'):
            clickx1 = xmin + 6*dimensionxbox + centerxbox
        elif(moves[0] == 'a'):
            clickx1 = xmin + 7*dimensionxbox + centerxbox
        
        if(moves[1] == '8'):
            clicky1 = ymax - centerybox
        elif(moves[1] == '7'):
            clicky1 = ymax - dimensionybox - centerybox
        elif(moves[1] == '6'):
            clicky1 = ymax - 2*dimensionybox - centerybox
        elif(moves[1] == '5'):
            clicky1 = ymax - 3*dimensionybox - centerybox
        elif(moves[1] == '4'):
            clicky1 = ymax - 4*dimensionybox - centerybox
        elif(moves[1] == '3'):
            clicky1 = ymax - 5*dimensionybox - centerybox
        elif(moves[1] == '2'):
            clicky1 = ymax - 6*dimensionybox - centerybox
        elif(moves[1] == '1'):
            clicky1 = ymax - 7*dimensionybox - centerybox
        
        if(moves[2] == 'h'):
            clickx2 = xmin + centerxbox
        elif(moves[2] == 'g'):
            clickx2 = xmin + dimensionxbox + centerxbox
        elif(moves[2] == 'f'):
            clickx2 = xmin + 2*dimensionxbox + centerxbox
        elif(moves[2] == 'e'):
            clickx2 = xmin + 3*dimensionxbox + centerxbox
        elif(moves[2] == 'd'):
            clickx2 = xmin + 4*dimensionxbox + centerxbox
        elif(moves[2] == 'c'):
            clickx2 = xmin + 5*dimensionxbox + centerxbox
        elif(moves[2] == 'b'):
            clickx2 = xmin + 6*dimensionxbox + centerxbox
        elif(moves[2] == 'a'):
            clickx2 = xmin + 7*dimensionxbox + centerxbox
        
        if(moves[3] == '8'):
            clicky2 = ymax - centerybox
        elif(moves[3] == '7'):
            clicky2 = ymax - dimensionybox - centerybox
        elif(moves[3] == '6'):
            clicky2 = ymax - 2*dimensionybox - centerybox
        elif(moves[3] == '5'):
            clicky2 = ymax - 3*dimensionybox - centerybox
        elif(moves[3] == '4'):
            clicky2 = ymax - 4*dimensionybox - centerybox
        elif(moves[3] == '3'):
            clicky2 = ymax - 5*dimensionybox - centerybox
        elif(moves[3] == '2'):
            clicky2 = ymax - 6*dimensionybox - centerybox
        elif(moves[3] == '1'):
            clicky2 = ymax - 7*dimensionybox - centerybox
    
    #print(clickx1)
    #print(clicky1)
    #print(clickx2)
    #print(clicky2)
    pyautogui.moveTo(clickx1, clicky1)
    pyautogui.mouseDown()
    k = random.randrange(0, 1000000)%(waiting*10000)/1000000
    time.sleep(k)
    pyautogui.mouseUp(clickx2, clicky2)
