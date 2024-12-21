# Gemstone_Price_Prediction
MLOPS project

## Step1 : Setting up the environment by following either of the process

### Option 1: Running init_setup.sh

```
If linux has conda in it then run below command 
1. bash init_setup.sh

In windows system we need to install unbuntu by running command  
2. wsl --install -d Ubuntu
3. Enter userid and password for linux

Then Install conda following below steps
4. wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
5. bash Miniconda3-latest-Linux-x86_64.sh
6. source ~/.bashrc
7. bash init_setup.sh
```

### Option 2: Running installation command manually
```
1. conda create  --prefix ./gemstone_env python=3.11.4 -y
2. conda activate "D:\Study\Data Science\MLOPS\Gemstone_Price_Prediction\gemstone_env"  
3. pip install -r requirements_dev.txt
```