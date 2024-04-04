import pandas as pd
import os 
import cv2
dataframe = pd.DataFrame(columns=['Files'])

path = "/media/gratus/HDD/TRS/paddleocr/CNN letter Dataset"

dirs = os.listdir(path)


i=0
for dir in dirs:
    files= pd.append(dir)


print(pd)