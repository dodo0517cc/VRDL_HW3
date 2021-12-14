import json
from PIL import Image
import os
import numpy as np
answer = []
with open('/Users/dodo/Desktop/深度學習之視覺辨識/VRDL_HW3/coco_instances_results.json', newline='') as jsonfile:
    data = json.load(jsonfile)
    for i in range(len(data)):
        category_id = data[i]['category_id'] + 1
        score = data[i]['score']
        image_id = data[i]['image_id'] + 1
        bbox = data[i]['bbox']
        segmentation = data[i]['segmentation']

        answer.append({
            'image_id' : image_id,
            'score' : score,
            'category_id' : category_id,
            'bbox' : bbox,
            'segmentation' : segmentation})
print(len(answer))
os.chdir('/Users/dodo/Desktop/深度學習之視覺辨識/VRDL_HW3/')
with open('answer.json', 'w') as f:
    json.dump(answer,f)