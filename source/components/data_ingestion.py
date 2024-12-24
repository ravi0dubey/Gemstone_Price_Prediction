import sys
import os
import pandas as pd
import numpy as np
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from pathlib import Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from source.logger.logger import logging    
from source.exception.exception import customexception

@dataclass
class DataIngestionConfig:
    def __init__(self):
        pass

class DataIngestion:
    def __init__(self):
        pass
    def initiate_data_ingestion(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise customexception(e,sys)
