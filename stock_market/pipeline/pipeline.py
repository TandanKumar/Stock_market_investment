from stock_market.config.configuration import Configuartion
from stock_market.logger import logging
from stock_market.exception import stockmarketException

from stock_market.entity.artifact_entity import DataIngestionArtifact
from stock_market.entity.config_entity import DataIngestionConfig
from stock_market.component.data_ingestion import DataIngestion
import os,sys


class Pipeline:
    

    def __init__(self, config: Configuartion = Configuartion()    ) :
        try:
            
            self.config = config
        except Exception as e:
            raise stockmarketException(e, sys) from e

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise stockmarketException(e, sys) from e

    
        
    def run_pipeline(self):
        try:
            #data Ingestion
            data_ingestion_artifact = self.start_data_ingestion()

        except Exception as e:
            raise stockmarketException(e,sys) from e