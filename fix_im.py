from PIL import ImageGrab
from utils import *
import numpy as np
import time
import cv2

counter = 0
pic0 = np.array(ImageGrab.grab(bbox=(1, 329, 610, 1390)))
cv2.imwrite('4/'+str(counter)+'.png', pic0)




