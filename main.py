from sensor.pipeline.training_pipeline import TrainingPipeline
from sensor.exception import SensorException
import os
import sys
from sensor.logger import logging
from sensor.utils2 import dump_csv_file_to_mongodb_collection


def test_exception():
    try:
        logging.info("error occured division by zero")
        a=1/0
    except Exception as e:
        raise SensorException(e,sys)





if __name__ == "__main__":

    try:
        logging.info("Starting application")

        pipeline = TrainingPipeline()

        pipeline.run_pipeline()

        logging.info("Pipeline execution completed")

    except Exception as e:
        raise SensorException(e, sys)





