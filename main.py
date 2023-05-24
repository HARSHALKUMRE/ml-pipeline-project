import os, sys
import pandas as pd
import numpy as np
from income.constant import *
from income.logger import logging
from income.exception import IncomeException
from income.pipeline.training_pipeline import TrainingPipeline

def main():
    try:
        pipeline = TrainingPipeline()
        pipeline.run_pipeline()
    except Exception as e:
        logging.error(f"{e}")

if __name__ == "__main__":
    main() 