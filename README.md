# Gemstone_Price_Prediction
MLOPS project

Step1 : Setting up the environment  by following either of the process

Option 1: 
If linux has conda in it then run below command 
bash init_setup.sh

In windows system we need to install unbuntu by running command  
wsl --install -d Ubuntu
enter userid and password for linux

Then Install conda following below steps
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
source ~/.bashrc

Then do the setup by running 
bash init_setup.sh


Option 1: We can directly run the command explicity

conda create  --prefix ./gemstone_env python=3.11.4 -y
conda activate "D:\Study\Data Science\MLOPS\Gemstone_Price_Prediction\gemstone_env"  
pip install -r requirements_dev.txt