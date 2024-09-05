from mlProject.utils.common import read_yaml,create_directories
from mlProject.constants import *


class ConfigurationManager:
    def __init__(self):
        self.config=read_yaml()
