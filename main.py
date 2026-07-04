from sensor.pipeline.training_pipeline import TrainingPipeline
from sensor.exception import SensorException
import os
import sys
from sensor.logger import logging
from sensor.utils2 import dump_csv_file_to_mongodb_collection
from fastapi import FastAPI
from sensor.constant.application import APP_HOST,APP_PORT
from starlette.responses import RedirectResponse
from uvicorn import run as app_run
from fastapi.responses import Response
from sensor.ml.model.estimator import ModelResolver,TargetValueMapping
from uvicorn import run as app_run
from sensor.utils.main__utils import load_object
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI,File,UploadFile,Response
import pandas as pd
from sensor.constant.training_pipeline import SAVED_MODEL_DIR
import yaml


app=FastAPI(title = "APS Fault Detection API")

origins = ["*"]
#Cross origin Resource Sharing(Cors)
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods =["*"],
    allow_headers = ["*"],
)



@app.get("/",tags=["authentication"])
async def index():
    return RedirectResponse(url ="/docs")





@app.get("/train")
async def train():
   try:
     training_pipeline = TrainingPipeline()

     if training_pipeline.is_pipeline_running:
         return Response("Training pipeline is already running.")
    
     training_pipeline.run_pipeline()
     return Response("Training succesfully completed!")
   
   except Exception as e:
       return Response(f"Error Occured!: {e}")





@app.get("/predict")
async def predict():
  try:
    #get data and from the csv file 
    #covert it to data frame
    df = pd.read_csv("prediction_file/prediction_input.csv")

    # convert all columns to float
    df = df.astype(float)
    model_resolver = ModelResolver(model_dir=SAVED_MODEL_DIR)
    if not model_resolver.is_model_exists():
        return Response("Model is not available")
    
    best_model_path = model_resolver.get_best_model_path()
    model = load_object(file_path=best_model_path)
    y_pred = model.predict(df)
    df['predicted_column'] = y_pred
    df['predicted_column'].replace(TargetValueMapping().reverse_mapping(), inplace = True)
# Save the output
    output_path = "prediction_file/prediction_output.csv"
    df.to_csv(output_path, index=False)
    print("SAVED_MODEL_DIR:", SAVED_MODEL_DIR)
    print("Model exists:", model_resolver.is_model_exists())

    return {
            "message": "Prediction completed successfully.",
            "predictions": df["predicted_column"].tolist()
        }


  except Exception as e:
     raise SensorException(e,sys) 

def test_exception():
    try:
        logging.info("error occured division by zero")
        a=1/0
    except Exception as e:
        raise SensorException(e,sys)

def main():
    try:

      training_pipeline = TrainingPipeline()

      training_pipeline.run_pipeline()
    
    except Exception as e:
        logging.exception(e)


if __name__ == "__main__":

   # try:
    #    logging.info("Starting application")


        

     #   logging.info("Pipeline execution completed")

    #except Exception as e:
      #  raise SensorException(e, sys)
    app_run(app,host=APP_HOST,port=APP_PORT)




