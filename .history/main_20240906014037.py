from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainPipeline
from mlProject.pipeline.stage_02_data_tranfomation import DataTransfomationpipeline
from mlProject.pipeline.stage_03_model_train import ModelTrainpipeline
from mlProject.pipeline.stage_04_model_evaluation import ModelEvaluationPipeline
from mlProject import logging


try:
    data_ingestion=DataIngestionTrainPipeline()
    data_ingestion.main()
    logging.info('Data Ingestion completed')
    print('*******************************')
except Exception as e:
    logging.exception(e)
    raise e     

try:
    data_transform=DataTransfomationpipeline()
    data_transform.main()
    logging.info('data_transform completed')
    print('*******************************')
except Exception as e:
    logging.exception(e)
    raise e     


try:
    model_train=ModelTrainpipeline()
    model_train.main()
    logging.info('data_transform completed')
    print('*******************************')
except Exception as e:
    logging.exception(e)
    raise e


try:
    model_evaluation=ModelEvaluationPipeline()
    model_evaluation.main()
    logging.info('data_transform completed')
    print('*******************************')
except Exception as e:
    logging.exception(e)
    raise e