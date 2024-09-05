import os,sys 
from mlProject import logging
from mlProject.entity.config_entity import *
import urllib.request
import zipfile

class DataIngestion:
        def __init__(self,config:DataIngestionConfig):
              self.config=config
              
        def dowmload_file(self):
            if not os.path.exists(self.config.local_data_path):
                urllib.request.urlretrieve(self.config.local_data_path,self.config.unzip_dir)
                logging.info('file downloaded')
                
            else:
                logging.info('file Already exists')    
                  
        def unzip_data(self):
            unzip_path=self.config.unzip_dir
            with zipfile.ZipFile (self.config.local_data_path,'r') as f:
                f.extractall(unzip_path)      