from mlProject.config.configuration import *
from mlProject.entity.config_entity import *
from mlProject.components.data_transfomation import DataTransfomation

class DataTransfomationpipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        Config=ConfigurationManager()
        data_transfomation_comfig=Config.get_data_transfomation_config()
        data_transform=DataTransfomation(config=data_transfomation_comfig)
        data_transform.train_test_split()