import os
import sys
from PIL import Image
import numpy as np
import json
os.chdir('/Users/dodo/Desktop/深度學習之視覺辨識/') 
data_path = os.listdir('./VRDL_HW3/test/')
del data_path[-1]
# del data_path[2]

for idx in range(len(data_path)):
    # load images ad masks
    path = data_path[idx]
    # img = Image.open('./VRDL_HW3/train/' + path + '/images/' + path + '.png').convert("RGB")
    # img.save(r'/Users/dodo/Desktop/深度學習之視覺辨識/VRDL_HW3/train_jpg/' + str(path) + '.jpg')
    img = Image.open('./VRDL_HW3/test/' + path).convert("RGB")
    img.save(r'/Users/dodo/Desktop/深度學習之視覺辨識/VRDL_HW3/test_jpg/' + str(path.split('.png')[0]) + '.jpg')