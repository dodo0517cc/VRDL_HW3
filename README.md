# VRDL_HW3 (Instance segmentation)

weights（model_final.pth)：https://drive.google.com/drive/folders/18wH4QouJC624e1c8YG0p9_dUsj6jptJH?usp=sharing
(Create a folder named output_test to save our results. Put the weight in the output_test file)

## Introduction

Instance segmentation includes classification, semantic segmentation and object detection. It is an extension of object detection, where a binary mask (i.e. object vs. background) is associated with every bounding box. The difference between semantic segmentation and instance segmentation is that semantic segmentation does not distinguish different instances belonging to the same category, but instance segmentation distinguishes different instances of the same type. For example, people below in the left-hand side are all marked in red, but are marked in different colors to distinguish different people in the right-hand side.

<img width="705" alt="image" src="https://user-images.githubusercontent.com/77607182/146368297-036d1106-e5ec-4c0f-b9cc-830ffdcb9544.png">

The current instance segmentation methods are divided into four types: top-down method based on object detection, bottom-up method based on semantic segmentation, integrated top-down and bottom-up, direct segmentation method, while the early instance segmentation method is biased towards top-down , Bottom-up.
In today’s homework, I will use Mask R-CNN for my model. It’s a top- down method based on object detection. The top-down method is to first obtain the object detection frame, and then perform mask prediction on the pixels in the frame.

## Model

The number of training images is small, only 24 images. It isn’t easy to train without using a pretrained model. As a result, I use the Mask R-CNN X101-FPN model to fine-tune the dataset. The table below is the results on the github of detectron2. Though Mask R-CNN X101-FPN model takes longer time to train, it can get a better performance.

<img width="392" alt="image" src="https://user-images.githubusercontent.com/77607182/146368581-84e4eb54-cc98-4cbd-96ad-29de9a92f4e3.png">

## Install Detectron2

STEP1: Install some requirements

    !pip install -q cython pyyaml==5.1
    !pip install -q -U 'git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI'

Step2: Download, compile, and install the Detectron2 package:

    !git clone https://github.com/facebookresearch/detectron2 detectron2_repo
    !pip install -q -e detectron2_repo

Step3: Restart the notebook runtime to continue

Step4: Install watermark and mmcv

    !pip install -q -U watermark
    %reload_ext watermark
    %watermark -v -p numpy,pandas,pycocotools,torch,torchvision,detectron2
    !pip install mmcv

Step5: Import packages we need, and set seed

Step6: Set up the config file and change the hyperparameters and path.

## Testing

Step7: Create another folder named annotated_results to save the test images with predictions.

Step8: Create a test dataframe in coco format sorted by specific order ["TCGA-A7-A13E-01Z-00-DX1.jpg", "TCGA-50-5931-01Z-00-DX1.jpg", "TCGA-G2-A2EK-01A-02-TSB.jpg", "TCGA-AY-A8YK-01A-01-TS1.jpg", "TCGA-G9-6336-01Z-00-DX1.jpg", "TCGA-G9-6348-01Z-00-DX1.jpg"]

Step9: Specificy the datasets. Use DefaultPredictor to predict the results.

Step10: Get the results in cocoformat using cocoevalutor.

    predictor = DefaultPredictor(cfg)
    evaluator = COCOEvaluator("nucleus_test", cfg, False, output_dir="./output_test/")
    val_loader = build_detection_test_loader(cfg, "nucleus_test")
    inference_on_dataset(predictor.model, val_loader, evaluator)

## Draw

Step11: Draw the results to check the correctness and save them.

![image](https://user-images.githubusercontent.com/77607182/145957936-28cb8d65-baee-43f7-8e9e-baab19cae9f3.png)

## Post-Processing

Step12: Cause the category of the results is automatically set to 0 and the image ids start in 0, we need to use ans.py to turn the catefory to 1 and plus 1 for all the image ids to submit the format for the homework. 

## Table of experimental results

<img width="415" alt="image" src="https://user-images.githubusercontent.com/77607182/146368770-245acd19-977d-4620-8ca6-8ebec1ac731e.png">
<img width="415" alt="image" src="https://user-images.githubusercontent.com/77607182/146368805-f95436c5-a271-4739-93a3-5b6933741bc5.png">


