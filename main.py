from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier import logging

STAGE_NAME = 'Data Ingestion stage'

try:
    logging.info(f">>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logging.info(">>>>>stage {STAGE_NAME} completed <<<<< \n\n X======X")
except Exception as e:
    logging.exception(e)
    raise e
