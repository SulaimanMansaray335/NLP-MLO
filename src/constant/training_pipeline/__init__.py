import os 
import sys
import numpy as np
import pandas as pd 

""""
Defining constant variables for Training Pipeline
"""
PIPELINE_NAME:str = "LSTM_Attention"
ARTIFACT_DIR:str = "artifacts"
TRAIN_FILE_NAME:str = 'samsum-train.csv'
TEST_FILE_NAME:str = 'samsum-test.csv'

SCHEMA_FILE_PATH:str = os.path.join("data_schema", "schema.yaml")

SAVED_MODEL_DIR = os.path.join("saved_models")
MODEL_FILE_NAME = 'nlpmodel.pk1' 


"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_DIR_NAME:str = "data_ingestion"
DATA_INGESTION_TRAIN_FILE_DIR:str = "train"
DATA_INGESTION_TEST_FILE_DIR:str = "test"
DATA_INGESTION_VALIDATION_DIR_NAME:str = "validation"

"""
Data Transformation related constant start with DATA_TRANSFORMATION VAR NAME
"""
DATA_TRANSFORMATION_DIR_NAME:str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR:str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR:str = "transformed_object"
PREPROCESSING_OBJECT_FILE_NAME:str = "preprocessor.pk1"

"""
Model_trainer
"""
MODEL_TRAINER_DIR_NAME:str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR:str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME:str = "nlpmodel.pk1"