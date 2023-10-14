from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier import logging
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_evaluation import EvaluationPipeline

STAGE_NAME = 'Data Ingestion stage'

try:
    logging.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logging.info(f">>>>>stage {STAGE_NAME} completed <<<<< \n\n X======X")
except Exception as e:
    logging.exception(e)
    raise e


STAGE_NAME = "Prepare base model"

try:
    logging.info(f'***************')
    logging.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    prepare_base_model =  PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logging.info(f">>>>>stage {STAGE_NAME} completed <<<<< \n\n X======X")

except Exception as e:
    logging.exception(e)
    raise e


STAGE_NAME = "Training"

try:
    logging.info(f"***************************")
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_trainer= ModelTrainingPipeline()
    model_trainer.main()
    logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nX===========X")

except Exception as e:
    logging.exception(e)
    raise e



STAGE_NAME = "Evaluation"

try:
    logging.info(f"***************************")
    logging.info(f">>>>>>> stage {STAGE_NAME} started<<<<<")
    model_evaluation= EvaluationPipeline()
    model_evaluation.main()
    logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<<\n\nX===========X")

except Exception as e:
    logging.exception(e)
    raise e