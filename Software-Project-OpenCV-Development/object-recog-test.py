from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep
from imutils.video import VideoStream
import datetime
import argparse
import imutils
import cv2
import numpy as np

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--picamera", type=int, default=-1,
	help="whether or not the Raspberry Pi camera should be used")
args = vars(ap.parse_args())

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

#cam=cv2.VideoCapture(0)
'''
cam = PiCamera()
cam.resolution = (640, 480)
cam.framerate = 32
cam.start_recording('objreq_video.h264')
cam.wait_recording(60)
cam.stop_recording()
'''
#rawCapture = PiRGBArray(cam, size=(640, 480))

# allow the camera to warmup
#sleep(0.5)

# initialize the video stream and allow the camera sensor to warmup
vs = VideoStream(usePiCamera=args["picamera"] > 0).start()
sleep(2.0)

while True:
#for frame in cam.capture_continuous(rawCapture, format="bgr", use_video_port=True):    
    frame = vs.read()
    frame = imutils.resize(frame, width=300)
    queryImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
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
        
        cv2.polylines(frame,[np.int32(queryBorder)], True, (0,255,0), 5)
    else:
        print "Not enough matches found - %d/%d"%(len(goodMatch), MIN_MATCH_COUNT)
        matchStatus = None
        
    # Draw the timestamp on the frame
    timestamp = datetime.datetime.now()
    ts = timestamp.strftime("%A %d %B %Y %I:%M:%S%p")
    cv2.putText(frame, ts, (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,
            	0.35, (0, 255, 0), 1)
    
    # Create the video feed window frame
    cv2.imshow('PuzNLuk', frame)
    
    # If 'q' is pressed, break from the loop
    if cv2.waitKey(10) == ord('q'):
        break

#cam.release()

# Do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()