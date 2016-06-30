import pyscreenshot
import os
import time
from globals import IMG_TL_X, IMG_TL_Y, IMG_LEN_X, IMG_LEN_Y

def get_screen():
    box = (IMG_TL_X, IMG_TL_Y,
           IMG_TL_X + IMG_LEN_X, IMG_TL_Y + IMG_LEN_Y)
    im = pyscreenshot.grab(box)
    im.save(os.getcwd() + '/screenshots/snap_' + str(int(time.time())) +
            '.png', 'PNG')
