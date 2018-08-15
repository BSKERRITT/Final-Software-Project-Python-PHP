# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import datetime
import time
import cv2
import numpy as np
 
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 24
rawCapture = PiRGBArray(camera, size=(320, 240))
 
# allow the camera to warmup
time.sleep(0.1)

MIN_MATCH_COUNT = 30

# Import training image
trainImg = cv2.imread("TrainingData/training.jpg",0)

# Initiate SIFT detector
siftDetector = cv2.xfeatures2d.SIFT_create()

# Find the keypoints and descriptors
trainKP, trainDesc = siftDetector.detectAndCompute(trainImg,None)

FLANN_INDEX_KDTREE = 1
flann_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
flann = cv2.FlannBasedMatcher(flann_params,{})
 
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array
    queryImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    queryKP, queryDesc = siftDetector.detectAndCompute(queryImg, None)
    
    matches = flann.knnMatch(queryDesc, trainDesc, k=2)

    goodMatch = []
    for m,n in matches:
        if(m.distance < 0.8*n.distance):
            goodMatch.append(m)
            
    if(len(goodMatch) > MIN_MATCH_COUNT):
        print "Correct object detected - %s"%trainImg.dtype
        tp = []
        qp = []
        for m in goodMatch:
            tp.append(trainKP[m.trainIdx].pt)
            qp.append(queryKP[m.queryIdx].pt)
        tp,qp = np.float32((tp,qp))
        H, status = cv2.findHomography(tp, qp, cv2.RANSAC, 3.0)
        matchStatus = status.ravel().tolist()
        
        h, w = trainImg.shape
        
        trainBorder = np.float32([[[0,0],[0,h-1],[w-1,h-1],[w-1,0]]])
        queryBorder = cv2.perspectiveTransform(trainBorder, H)
        
        cv2.polylines(image,[np.int32(queryBorder)], True, (0,255,0), 5)
    else:
        print "Not enough matches found - %d/%d"%(len(goodMatch), MIN_MATCH_COUNT)
        matchStatus = None
        
    # Draw the timestamp on the frame
    timestamp = datetime.datetime.now()
    ts = timestamp.strftime("%A %d %B %Y %I:%M:%S%p")
    cv2.putText(image, ts, (10, image.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,
            	0.35, (0, 255, 0), 1)
    
    # Create the video feed window frame
    cv2.imshow('PuzNLuk', image)
    
    # If 'q' is pressed, break from the loop
    if cv2.waitKey(10) == ord('q'):
        break
 
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

# Do a bit of cleanup
cv2.destroyAllWindows()