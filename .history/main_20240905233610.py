from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainPipeline
from mlProject import logging


try:
    data_ingestion=DataIngestionTrainPipeline()
    data_ingestion.main()
    logging.info('Data Ingestion completed')
except Exception as e:
    logging.exception(e)
    raise e     


