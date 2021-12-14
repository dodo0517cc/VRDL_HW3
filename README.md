# VRDL_HW3

weights（model_final.pth)：https://drive.google.com/drive/folders/18wH4QouJC624e1c8YG0p9_dUsj6jptJH?usp=sharing

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

Step5: Import packages we need

Step6: Load in json file which is turned into coco format

