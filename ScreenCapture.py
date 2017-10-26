#S C R E E N - C A P T U R E

import time
import numpy as np
import wx

app = wx.App()
screen = wx.ScreenDC()

# Used to time screenshot intervals
def timeit(f):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        ret = f(*args, **kwargs)    
        print('Seconds elapsed: {}'.format(time.time()-t1))
        return ret
    return wrapper

def screenshot(region=None):
    global screen

    assert type(region) is tuple
    assert len(region) == 4

    # Region is a tuple of (x, y, w, h)
    x = region[0]
    y = region[1]
    w = region[2]
    h = region[3]

    # Construct a bitmap
    bmp = wx.Bitmap(w, h)

    # Fill bitmap delete memory (don't want memory leak)
    mem = wx.MemoryDC(bmp)
    mem.Blit(0, 0, w, h, screen, x, y)
    del mem

    # Convert bitmap to image
    wxB = bmp.ConvertToImage()

    # Get data buffer
    img_data = wxB.GetData()

    # Construct np array from data buffer and reshape it to img
    img_data_str = np.frombuffer(img_data, dtype='uint8')
    img = img_data_str.reshape((h, w, 3))
    return img



# P R E - P R O C E S S I N G

import cv2
    
mser = cv2.MSER_create()
#img = cv2.imread('signboard.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
vis = img.copy()
regions, _ = mser.detectRegions(gray)
hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]
cv2.polylines(vis, hulls, 1, (0, 255, 0))
cv2.imshow('img', vis)
if cv2.waitKey(0) == 9:
    cv2.destroyAllWindows()
  
mask = np.zeros((img.shape[0], img.shape[1], 1), dtype=np.uint8)
for contour in hulls:
    cv2.drawContours(mask, [contour], -1, (255, 255, 255), -1)
    
text_only = cv2.bitwise_and(img, img, mask=mask)
     


# O C R
    
# import the necessary packages
from PIL import Image
import pytesseract
import os

# check to see if we should apply thresholding to preprocess the
# image
gray = cv2.threshold(gray, 0, 255,
	cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
 
# make a check to see if median blurring should be done to remove
# noise
#gray = cv2.medianBlur(gray, 3)

# write the grayscale image to disk as a temporary file so we can
# apply OCR to it
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)


# T R A N S L A T I O N

from google.cloud import translate

# Instantiates a client
translate_client = translate.Client()

# The text to translate

# The target language
target = 'en'

# Translates some text into Russian
translation = translate_client.translate(
    text,
    target_language=en)

print(u'Text: {}'.format(text))
print(u'Translation: {}'.format(translation['translatedText']))

# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)

