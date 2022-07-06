# Computer Vision

## Introduction
The first part of the project is called keypoints detection and CNN designing. In this part, I used 10 pictures as my sample pictures, and using two different keypoints detection methods "SIFT" and "Harris". I used these two methods and found 200 keypoints in each sample pictures and generated SIFT_patches.pth and Harris_patches.pth files. After that, I modified the sample CNN by adding some convolution layers and generated CNN2 and CNN3. The "CNN_Training_Result.pdf" presents the training result by setting different kinds of learning rate and batch sizes.

The second part of the project is images matching. There are two files in images_retrieval file, "query" and "images". "query" includes 34 pictures and each of the pictures is different, while "images" includes 4 * 34 = 136 pictures. Every four pictures in images file is corresponding to a picture in query file. The core idea is to fetch the top 20 keypoints in each picture in both images and query files; compute the cost matrix, and finally determine the best 4 fitting pictures from images file.  


## Start to install Pytorch environment
### 1. Download and install linux environment (Ubuntu) or connect to other servers  
### 2. Download Miniconda3  
Go to https://docs.conda.io/en/latest/miniconda.html and download suitable version, below is the suitable version for the writer.
```
bash Miniconda3-py39_4.11.0-Linux-x86_64.sh
```
### 3. Create Conda on your local machine  
Note: "myenv" can be any word that you want to name as your environment. 
```
conda create -n myenv python=3.6
```
Switch your environment from base to your setting environment.
```
conda activate myenv
```
### 4. Install jupyterlab
After switching to myenv, install jupyterlab by running the following code.
```
pip install jupyterlab
```
```
jupyter notebook --generate-config
```
Setup your password for login jupyter notebook.
```
jupyter notebook password
```
Be sure to remember the password for opening your jupyter notebook. Next section will guide you how to use the jupyter notebook.

### 5. Open your jupyter notebook
Set a port for your jupyter notebook, here is the example of setting the port
```
jupyter lab --no-browser --port=8888 --ip=0.0.0.0
```
Open your browser and it will ask you the password that you just set.
```
http://localhost:8888
```

### 6. Install some required packages
Export the below files
```
export PATH=/usr/local/common/gcc-7.3.0/bin:$PATH
export PATH=/usr/local/common/gcc-7.3.0/bin/g++:$PATH
export LD_LIBRARY_PATH=/usr/local/common/gcc-7.3.0/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/usr/local/common/gcc-7.3.0/lib64:$LD_LIBRARY_PATH
export PATH=/usr/local/eecsapps/cuda/cuda-10.1/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/eecsapps/cuda/cuda-10.1/lib64:$LD_LIBRARY_PATH
```
Check your nvcc version
```
nvcc --version (Not required)
```
Install pytorch with cuda10.1 to myenv
```
pip install torch==1.8.1+cu101 torchvision==0.9.1+cu101 torchaudio==0.8.1 -f https://download.pytorch.org/whl/torch_stable.html
```
Install related packages to your local machine
```
pip install opencv-contrib-python
conda install -n myenv -c conda-forge pandas
conda install -n myenv -c conda-forge matplotlib
conda install -n myenv -c conda-forge tqdm
pip install tensorboard_logger
```
### 7. Run the code
Drag all the files from Codes into your jupyter notebook. Run keypoint_detection.ipynb and keypoint_CNN_training.ipynb orderly to accomplish the first part, and run images_matching1.ipynb and images_matching2.ipynb to accomplish the second part of the project.  
## Result
![image](https://github.com/ironman850722/Computer_Vision/blob/main/Matching_Precision.jpg)  
In the figure, when finding the most matching picture among 136 pictures in images file, the average correctness rate is 58.8%; when finding the four most matching pictures among 136 pictures in image file, the average correctness rate is 40.4%. However, if we randomly pick 1 or 4 pictures in images file, the average correctness rate is only 2.9%.







