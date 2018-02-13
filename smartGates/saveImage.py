import cv2
import time
import database
import regOcr

def saveImage(image):
    current = str(time.time())
    imagePath = 'smartGates//regpPhotos//ocvi_' + current + '_edges.jpg'
    cv2.imwrite(imagePath, image)
    processImage(imagePath)
    print "Pictures saved"

def processImage(photoId):

    text = regOcr.getRegistrationNumber(photoId)
    if(text != ""):
        print text
        database.Database_access(text)
        print "text recognized"






