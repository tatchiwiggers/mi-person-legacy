from pydantic import BaseModel

class Sentiment(BaseModel):
    sentence: str
    
class SentimentRespose(Sentiment):
    pass