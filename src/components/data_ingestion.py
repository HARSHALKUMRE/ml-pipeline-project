import os, sys
import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    raw_data_path = os.path.join("artifacts", "raw.csv")
    train_data_path = os.path.join("artifacts", "train.csv")
    test_data_path = os.path.join("artifacts", "test.csv")


class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info(f"Data Ingestion Started.")
        try:
            logging.info("Data Reading Stared from local system")
            data = pd.read_csv(os.path.join("notebooks/data", "income_cleandata.csv"))
            logging.info("Data Reading completed.")

            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_path), exist_ok=True)
            data.to_csv(self.data_ingestion_config.raw_data_path, index=False)
            logging.info("Data is splitted into train and test sets.")

            train_set, test_set = train_test_split(data, test_size=0.30, random_state=42)

            train_set.to_csv(self.data_ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.data_ingestion_config.test_data_path, index=False, header=True)

            logging.info("Data Ingestion Completed.")

            return (
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path
            )
        except Exception as e:
            logging.info("Error Occured in data ingestion stage.")
            raise CustomException(e, sys) from e    


if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()