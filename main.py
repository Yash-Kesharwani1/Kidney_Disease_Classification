from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.exception import CustomException
from cnnClassifier.pipeline.stage_03_training_model import ModelTrainingPipeline

STAGE_NAME = 'Data Ingestion stage'

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx=======================x")
except CustomException as e:
    logger.exception(e)
    raise e



STAGE_NAME = 'Prepare base model'
try:
    logger.info(f"***************************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx===========================x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Training'
try:
    logger.info(f"*********************************")
    logger.info(f'>>>>>>> stage {STAGE_NAME} started <<<<<<<<<')
    obj = ModelTrainingPipeline()
    logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx=========================x")
except CustomException as e:
    logger.exception(e)
    raise e