import importlib
miperson = importlib.import_module("mi-person")

from http.client import HTTPException
from fastapi import FastAPI, Depends, status
from fastapi.security import HTTPBearer
from .ml_logic import model


app = FastAPI()

    
@app.get('/mi-person')    
def analyze(sentence: str):
    result = model.sentiment_scores(sentence)
    return result
