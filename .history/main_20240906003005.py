from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainPipeline
from mlProject.pipeline.stage_02_data_tranfomation import DataTransfomationpipeline
from mlProject import logging


try:
    data_ingestion=DataIngestionTrainPipeline()
    data_ingestion.main()
    logging.info('Data Ingestion completed')
except Exception as e:
    logging.exception(e)
    raise e     

try:
    data_transform=DataTransfomationpipeline()
    data_transform.main()
    logging.info('data_transform completed')
except Exception as e:
    logging.exception(e)
    raise e     
