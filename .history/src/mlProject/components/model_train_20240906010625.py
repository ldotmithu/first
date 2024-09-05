from mlProject.config.configuration import *
import pandas as pd 

class ModelTrain:
    def __init__(self,config:ModelTrainConfig) -> None:
        self.config=config
        
    def train(self):
        train_data=pd.read_csv(self.config.train_data_path)
        test_data=pd.read_csv(self.config.test_data_path)
        
        target_col='Outcome'
        
        X_train=train_data.drop(columns=[target_col],axis=1)
        X_test=test_data[target_col]
        y_train=train_data.drop(columns=[target_col],axis=1)
        y_test=test_data[target_col]
        