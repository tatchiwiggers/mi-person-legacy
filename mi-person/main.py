import importlib

miperson = importlib.import_module("mi-person")

from database import query_user  
from http.client import HTTPException
from fastapi import FastAPI, Depends, status
from fastapi.security import HTTPBearer
from fastapi_login import LoginManager
# from miperson.db.database import query_user
from ml_logic import model
from models import SentimentRespose

from typing import Union

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException


app = FastAPI()
# security = HTTPBearer()
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# SECRET = "0680afeeaa528c097e19f4c497fe99d4770c82c2c443243a"
# manager = LoginManager(SECRET, '/login')


# @app.post('/login')
# def login(data: OAuth2PasswordRequestForm = Depends()):
#     email = data.username
#     password = data.password

#     user = query_user(email)
#     if not user:
#         # you can return any response or error of your choice
#         raise InvalidCredentialsException
#     elif password != user['password']:
#         raise InvalidCredentialsException

#     access_token = manager.create_access_token(
#         data={'sub': email}
#     )
#     return {'access_token': access_token}
    
    
# @app.get('/proteced')
# def protected_route(user=Depends(manager)):
#     return {'user': user}
    
    
@app.get('/mi-person')    
def analyze(sentence: str):
    result = model.sentiment_scores(sentence)
    return result
