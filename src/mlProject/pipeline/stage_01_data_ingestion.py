from mlProject.config.configuration import *
from mlProject.components.data_ingestion import DataIngestion

class DataIngestionTrainPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        Config=ConfigurationManager()
        data_ingestion_config=Config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.dowmload_file()
        data_ingestion.unzip_data()