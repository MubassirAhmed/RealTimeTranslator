#S C R E E N - C A P T U R E

import numpy as np
import wx
from PIL import Image



def screenshot(region=None):
    global screen

    app = wx.App()
    screen = wx.ScreenDC()

    w, h = screen.Size.Get()

    # Construct a bitmap
    bmp = wx.Bitmap(w, h)

    # Fill bitmap delete memory (don't want memory leak)
    mem = wx.MemoryDC(bmp)
    mem.Blit(0, 0, w, h, screen, 0, 0)
    del mem

    # Convert bitmap to image
    wxB = bmp.ConvertToImage()
    
    
    # Get data buffer
    img_data = wxB.GetData()

    # Construct np array from data buffer and reshape it to img
    img_data_str = np.frombuffer(img_data, dtype='uint8')
    img = img_data_str.reshape((h, w, 3))

    #Converts np array image back to PIL image
    img = Image.fromarray(img)
    return img

"""
def main():
    screenshot().show()


if __name__ == "__main__":
    main()

""