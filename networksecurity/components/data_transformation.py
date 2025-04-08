import sys
import os
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline
import numpy as np

from networksecurity.constants.training_pipeline import TARGET_COLUMN
from networksecurity.constants.training_pipeline import DATA_TRANSFORMATION_IMPUTER_PARAMS

from networksecurity.entity.artifact_entity import (DataValidationArtifact,DataTransformationArtifact)

from networksecurity.entity.config_entity import DataTransformationConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.utils.main_utils.utils import  save_numpy_array_data,save_object

class DataTransformation:
    def __init__(self,data_validation_artifcat:DataValidationArtifact,data_transformation_config:DataTransformationConfig):
        try:
            self.data_validation_artifact:DataValidationArtifact = data_validation_artifcat
            self.data_transformation_config:DataTransformationConfig = data_transformation_config
            
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    @staticmethod
    def read_data(file_path) ->pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise  NetworkSecurityException(e,sys)
    
    def get_transformer_object(cls)->Pipeline:
        """
        it initializes a KNN imputer with the parameters specified in the training_pipeline.py file
        and returns a pipleine object with the knn imputer object as first step.
        
        Args:
        cls:pipeline
        
        returns:
        A pipeline object
        """
        
        logging.info("entered get_data_transformer_object method of transformation class")
        try:
            imputer:KNNImputer = KNNImputer(**DATA_TRANSFORMATION_IMPUTER_PARAMS)
            logging.info("KNN imputer intializes with(DATA_TRANSFORMATION_IMPUTER_PARAMS) ")
            
            processor:Pipeline= Pipeline([("imputer",imputer)])
            return processor
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)
            
        
        
        
        
    def initiate_data_transformation(self)->DataTransformationArtifact:
        logging.info("Entered initaite_data_transformation method of DataTransformation class")
        try:
            logging.info("starting data transformation")
            train_df = DataTransformation.read_data(self.data_validation_artifact.valid_train_file_path)
            test_df = DataTransformation.read_data(self.data_validation_artifact.valid_test_file_path)
            
            ##training df
            input_features_train_df = train_df.drop(columns=[TARGET_COLUMN],axis = 1)
            target_features_train_df = train_df[TARGET_COLUMN]
            
            #encoding target features with (1,0)
            target_features_train_df = target_features_train_df.replace(-1,0)
            
                    ##testing df
            input_features_test_df = test_df.drop(columns=[TARGET_COLUMN],axis = 1)
            target_features_test_df = test_df[TARGET_COLUMN]
            
            #encoding target features with (1,0)
            target_features_test_df = target_features_test_df.replace(-1,0)
            
            preprocessor = self.get_transformer_object()
            
            preprocessor_object = preprocessor.fit(input_features_train_df)
            transformed_input_train_feature = preprocessor_object.transform(input_features_train_df)
            transformed_input_test_feature = preprocessor_object.transform(input_features_test_df)
            
            ##combining into an array broth train,test features
            
            train_arr = np.c_[transformed_input_train_feature,np.array(target_features_train_df)]
            test_arr = np.c_[transformed_input_test_feature,np.array(target_features_test_df)]
            
            
            ##saving numpy array data
            save_numpy_array_data(self.data_transformation_config.transformed_train_file_path,array= train_arr,)
            save_numpy_array_data(self.data_transformation_config.transformed_test_file_path,array= test_arr,)
            save_object(self.data_transformation_config.transformed_object_file_path,preprocessor_object,)
            
            ##preparing artifacts
            
            data_transformation_artifact=DataTransformationArtifact(
                transformed_object_file_path=self.data_transformation_config.transformed_object_file_path,
                transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
                transformed_test_file_path=self.data_transformation_config.transformed_test_file_path
            )
            return data_transformation_artifact
            
            
            
            
        except Exception as e:
            raise NetworkSecurityException(e,sys)