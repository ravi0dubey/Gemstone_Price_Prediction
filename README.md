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
4. pip install dvc
5. dvc init
```

## Step2 : Data Version Control
Run below commands to do version control of gemstone.csv file
'''
1. dvc add dataset/gemstone.csv
'''
![image](https://github.com/user-attachments/assets/4a2160ef-7802-4b6a-a5f3-a0decf0372c9)


## Step3 : Run Training Pipeline
To train the model follow below steps
```
1. mlflow server --host 127.0.0.1 --port 7070(It needs to be executed in one terminal and it should keep on running)
2. python .\source\pipeline\training_pipeline.py (run it in separate terminal)
```

On running the **Training Pipeline** you will get below output and the url to see the Experiments results in MLFLOW. Click on the url http://127.0.0.1:7070/#/experiments/0/runs/9b8d411fd2104a91903594a227cf70ff to see the experiments output

```
D:\Study\Data Science\MLOPS\Gemstone_Price_Prediction\new_env\Lib\site-packages\setuptools\_distutils\__init__.py
http
2024/12/26 10:42:58 WARNING mlflow.models.model: Model logged without a signature and input example. Please set `input_example` parameter when logging the model to auto infer the model signature.
Registered model 'ml_model' already exists. Creating a new version of this model...
2024/12/26 10:42:59 INFO mlflow.store.model_registry.abstract_store: Waiting up to 300 seconds for model version to finish creation. Model name: ml_model, version 3
Created version '3' of model 'ml_model'.
🏃 View run welcoming-boar-13 at: http://127.0.0.1:7070/#/experiments/0/runs/9b8d411fd2104a91903594a227cf70ff
🧪 View experiment at: http://127.0.0.1:7070/#/experiments/0
```

This is how the Experiments should look in **MLFLOW**
![image](https://github.com/user-attachments/assets/ddbff8a6-d329-46bf-820e-93982abb2baf)
**The Metrices**
![image](https://github.com/user-attachments/assets/5c5ef678-70d1-46fe-a731-68c99e123a3b)

**The Artifacts**
![image](https://github.com/user-attachments/assets/5ec294e0-daa2-4552-9d23-6910342945ff)


## Step3 : Prediction
To see the prediction of prices following below steps
```
1. python .\app.py
2. run http://localhost:8012/ to see the main screen
3. copy http://localhost:8012/predict to new window
4. Enter the different input values and then press Submit button
5. You should see predicted price of stone.
```
**Home Screen** of Diamond Prediction
![image](https://github.com/user-attachments/assets/355886b8-bcf3-45d9-99e9-035afa863d20)

</n> Enter details in **Prediction screen** and click on Submit button </n> !Enering the Values


![image](https://github.com/user-attachments/assets/2bee32fe-8afc-45a1-9db9-a34c551d3dd7)

</n> We will get the price as show below </n>
![image](https://github.com/user-attachments/assets/74d75916-581a-47c7-a1e1-76fa8f45c035)




