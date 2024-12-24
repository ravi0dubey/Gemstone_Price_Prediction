
import sys
import os
import pandas as pd
import numpy as np
from dataclasses import dataclass
from pathlib import Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from source.logger.logger import logging    
from source.exception.exception import customexception
from source.utils.utils import save_object
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OrdinalEncoder,StandardScaler


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()
    
    def get_data_transformation(self):    
        try:
            logging.info('Data Transformation initiated')
            """
            Define which columns should be ordinal-encoded and which should be scaled
            """
            categorical_cols = ['cut', 'color','clarity']
            numerical_cols = ['carat', 'depth','table', 'x', 'y', 'z']
            """
            Define the custom ranking for each ordinal variable
            """
            cut_categories = ['Fair', 'Good', 'Very Good','Premium','Ideal']
            color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']
            logging.info('Pipeline Initiated')
            
            """
            Numerical Pipeline
            """
            num_pipeline=Pipeline(
                steps=[
                ('imputer',SimpleImputer(strategy='median')),
                ('scaler',StandardScaler())
                ]
            )
            
            """
            Categorigal Pipeline
            """
            cat_pipeline=Pipeline(
                steps=[
                ('imputer',SimpleImputer(strategy='most_frequent')),
                ('ordinalencoder',OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories])),
                ('scaler',StandardScaler())
                ]
            )
            preprocessor=ColumnTransformer([
            ('num_pipeline',num_pipeline,numerical_cols),
            ('cat_pipeline',cat_pipeline,categorical_cols)
            ])
            return preprocessor
            
        except Exception as e:
            logging.info("Exception occured in the initiate_datatransformation")
            raise customexception(e,sys)
            
    
    def initialize_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            
            logging.info("Read train and test data complete")
            logging.info(f'Train Dataframe Head : \n{train_df.head().to_string()}')
            logging.info(f'Test Dataframe Head : \n{test_df.head().to_string()}')           
            preprocessing_obj = self.get_data_transformation()
            """ Since first column has no name we are dropping first column and its data """
            if train_df.columns[0] == " " or pd.isna(train_df.columns[0]):
                train_df.drop(train_df.columns[0], axis=1, inplace=True)
                test_df=test_df.drop(columns=columns_to_drop,axis=1)
            
            target_column_name = 'price'
            columns_to_drop = [target_column_name]
            """ dropping Dependent feature from Train input features and storing it as Target_Feature """
            input_feature_train_df = train_df.drop(columns=columns_to_drop,axis=1)
            target_feature_train_df=train_df[target_column_name]
            """ dropping Dependent feature from test input features and storing it as Target_Feature """
            input_feature_test_df=test_df.drop(columns=columns_to_drop,axis=1)
            target_feature_test_df=test_df[target_column_name]
            
            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)
            
            logging.info("Applying preprocessing object on training and testing datasets.")
            
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )
            
            logging.info("preprocessing pickle file saved")
            
            return (
                train_arr,
                test_arr
            )
            
        except Exception as e:
            logging.info("Exception occured in the initiate_datatransformation")

            raise customexception(e,sys)
            

if __name__=="__main__":
    data_transform_obj=DataTransformation()
    data_transform_obj.initialize_data_transformation('artifacts/train.csv','artifacts/test.csv')
