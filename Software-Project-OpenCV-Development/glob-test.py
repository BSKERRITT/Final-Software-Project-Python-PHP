import glob


im = glob.iglob('TrainingData/*.jpg')
if(im.next() == "TrainingData/training.jpg"):
    print im.next()
elif(im.next() == "TrainingData/training2.jpg"):
    print im.next()