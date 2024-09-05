from mlProject.config.configuration import *
from mlProject.components.model_train import *

class ModelTrainpipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        Config=ConfigurationManager()
        model_train_config=Config.get_model_train()
        model_train=ModelTrain(config=model_train_config)
        model_train.train()