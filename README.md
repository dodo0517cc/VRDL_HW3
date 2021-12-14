# VRDL_HW3

weights（model_final.pth)：https://drive.google.com/drive/folders/18wH4QouJC624e1c8YG0p9_dUsj6jptJH?usp=sharing
(Create a folder named output_test to save our results. Put the weight in the output_test file)

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

Step7: Create another folder named annotated_results to save the test images with predictions.

Step8: Create a test dataframe in coco format sorted by specific order ["TCGA-A7-A13E-01Z-00-DX1.jpg", "TCGA-50-5931-01Z-00-DX1.jpg", "TCGA-G2-A2EK-01A-02-TSB.jpg", "TCGA-AY-A8YK-01A-01-TS1.jpg", "TCGA-G9-6336-01Z-00-DX1.jpg", "TCGA-G9-6348-01Z-00-DX1.jpg"]

Step9: Specificy the datasets. Use DefaultPredictor to predict the results.

Step10: Get the results in cocoformat using cocoevalutor.

Step11: Draw the results to check the correctness and save them.

![image](https://user-images.githubusercontent.com/77607182/145957936-28cb8d65-baee-43f7-8e9e-baab19cae9f3.png)


