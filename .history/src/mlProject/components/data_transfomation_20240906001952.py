from mlProject.config.configuration import *
from sklearn.model_selection import train_test_split
import pandas as pd 
import os

class DataTransfomation:
    def __init__(self,config:DataTransfomationConfig):
        self.config=config
        
    def train_test_split(self):    
        data=pd.read_csv(self.config.data_path)
        
        train_data,teat_data=train_test_split(data,test_size=0.2)
        
        train_data.to_csv(os.path.join())