from mlProject.utils.common import read_yaml,create_directories
from mlProject.constants import *
from mlProject.entity.config_entity import *


class ConfigurationManager:
    def __init__(self):
        self.config=read_yaml(CONFIG_FILE_PATH)
        
        create_directories([self.config.artifacts_root])
        
    def get_data_ingestion_config(self):
        config=self.config.data_ingestion
        
        create_directories([config.root_dir])    
        
        data_ingestion_config=DataIngestionConfig(
            root_dir= config.root_dir,
            URL=config.URL,
            local_data_path=config.local_data_path,
            unzip_dir=config.unzip_dir
        )
        
        return data_ingestion_config
    
    def get_data_transfomation_config(self):
        config=self.config.data_transform
        
        create_directories([config.root_dir])
        
        data_ingestion_config=DataTransfomationConfig(
            root_dir=config.root_dir
        ) 