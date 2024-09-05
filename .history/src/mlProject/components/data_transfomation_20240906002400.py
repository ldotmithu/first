from mlProject.config.configuration import *
from sklearn.model_selection import train_test_split
import pandas as pd 
import os
from mlProject import logging

class DataTransfomation:
    def __init__(self,config:DataTransfomationConfig):
        self.config=config
        
    def train_test_split(self):    
        data=pd.read_csv(self.config.data_path)
        
        train_data,test_data=train_test_split(data,test_size=0.2)
        logging.info('split the data ')
        
        train_data.to_csv(os.path.join(self.config.root_dir,'train.csv'),index=False)
        test_data.to_csv(os.path.join(self.config.root_dir,'test.csv'),index=False)
        
        logging.info(train_data.shape)
        logging.info(test_data.shape)
        