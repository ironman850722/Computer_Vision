# Computer_Vision

## How to install Pytorch environment
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
Installing pytorch with cuda10.1 to myenv
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
