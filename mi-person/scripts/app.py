from fastapi import FastAPI
from model import sentiment_scores
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get('/')
def index():
    return {'message': 'deu bom'}

@app.get('/mi-person')    
def analyze(sentence: str):
    result = sentiment_scores(sentence)
    return result

