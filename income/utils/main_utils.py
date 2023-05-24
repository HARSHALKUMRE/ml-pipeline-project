import os, sys
import yaml 
import numpy as np
import dill
import pandas as pd
from income.constant import *
from income.exception import IncomeException
from income.logger import logging


def read_yaml_file(file_path:str) -> dict:
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise IncomeException(e, sys) from e