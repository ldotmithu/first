from mlProject.config.configuration import *
import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

class ModelTrain:
    def __init__(self,config:ModelTrainConfig) -> None:
        self.config=config
        
    def train(self):
        train_data=pd.read_csv(self.config.train_data_path)
        test_data=pd.read_csv(self.config.test_data_path)
        
        target_col='Outcome'
        
        X_train=train_data.drop(columns=[target_col],axis=1)
        y_test=test_data.drop(columns=[target_col],axis=1)
        y_train=train_data[target_col]
        y_test=test_data[target_col]
        
        rf = RandomForestClassifier(
    n_estimators=1000,
    criterion='entropy',
    max_depth=6,
    min_samples_split=4,
    min_samples_leaf=2,
    max_features='sqrt',
    bootstrap=True,
    n_jobs=-1,
    random_state=42
)
        
        rf.fit(X_train,y_train)
        
        joblib.dump(os.path.join(self.config.root_dir,self.config.model_name))
        
        
        
        