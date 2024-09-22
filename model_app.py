# import necessary libraries
#!pip install fastapi

from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np
import joblib

app = FastAPI()

class Input(BaseModel):
    CONSOLE: object
    YEAR: int
    CATEGORY: object
    PUBLISHER: object
    RATING: object
    CRITICS_POINTS: float
    USER_POINTS: float

class Output(BaseModel):
    SalesInMillions: float

@app.post("/predict")

def predict(data: Input) -> Output:
    #input
    X_input = pd.DataFrame([{'CONSOLE':  data.CONSOLE,'YEAR':  data.YEAR,'CATEGORY':  data.CATEGORY,'PUBLISHER':  data.PUBLISHER,'RATING':  data.RATING,'CRITICS_POINTS':  data.CRITICS_POINTS,'USER_POINTS':  data.USER_POINTS}])

    #Load the model
    model = joblib.load("video_games_sales_pipeline_model.pkl")

    #Predict using the model
    prediction = model.predict(X_input)
    
    #intercept = model.named_steps['model'].intercept_
    #slope = model.named_steps['model'].coef_
    
    #output
    #return Output(SalesInMillions = prediction, slope = slope, intercept = intercept)
    return Output(SalesInMillions = prediction)

# Execute this on the terminal using the command uvicorn model_app:app --reload
# use the local host url on web http://localhost:8000/docs or http://127.0.0.1:8000/docs


