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

## Step2 : Run Training Pipeline
To train the model following below steps
```
1. mlflow server --host 127.0.0.1 --port 7070(It needs to be executed in one terminal and it should keep on running)
2. python .\source\pipeline\training_pipeline.py (run it in separate terminal)
```

This is how the Experiments should look in MLFLOW
![image](https://github.com/user-attachments/assets/ddbff8a6-d329-46bf-820e-93982abb2baf)
The Metrices
![image](https://github.com/user-attachments/assets/5c5ef678-70d1-46fe-a731-68c99e123a3b)


